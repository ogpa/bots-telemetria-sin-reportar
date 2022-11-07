import requests
import urllib
from datetime import datetime
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import pandas as pd
import numpy as np
import os

COM_URL_BASE_CLOCATOR = "http://clocatorplus.comsatel.com.pe"
COM_URL_LOGIN = "http://clocatorplus.comsatel.com.pe/CL/faces/seguridad/login.xhtml"
COM_URL_FOUND = "http://clocatorplus.comsatel.com.pe/CL/faces/seguridad/login.xhtml;jsessionid="
COM_URL_MAIN = "http://clocatorplus.comsatel.com.pe/CL/faces/page/main.xhtml"
COM_URL_CLREPORTE = "http://clreportes.comsatel.com.pe/CLReporte/"
COM_URL_VEHICULOSINREPORTAR = "http://clreportes.comsatel.com.pe/CLReporte/faces/page/vehiculossinreportar/vehiculosSinReportarListar.xhtml"
USUARIO = "DPIZARRO"
CLAVE = "JDP9L9HKEYiQaXH"
COM_URL_BASE_CLREPORTES = "http://clreportes.comsatel.com.pe"
S3_BUCKET_NAME = "apps-innovacion-mbr"
S3_RUTA_FOLDER = "bi-telemetria/gps-sin-reportar/csv/"

# s3=boto3.resource("s3")

# def upload_file(file_name, bucket, object_name=None):
#     """Upload a file to an S3 bucket

#     :param file_name: File to upload
#     :param bucket: Bucket to upload to
#     :param object_name: S3 object name. If not specified then file_name is used
#     :return: True if file was uploaded, else False
#     """

#     # If S3 object_name was not specified, use file_name
#     if object_name is None:
#         object_name = os.path.basename(file_name)

#     # Upload the file
#     s3_client = boto3.client('s3')
#     try:
#         response = s3_client.upload_file(file_name, bucket, object_name)
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    # empieza a buscar el fin a partir del inicio
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def scan_comsatel(hoy):
    respLogin = requests.request("GET", COM_URL_LOGIN)
    # print(respLogin.headers)

    session_LogIn = extraer_texto(
        respLogin.headers["Set-Cookie"], "JSESSIONID=", "; Path=/CL;")
    # print(session_LogIn)

    cookieBarracuda_LogIn = extraer_texto(
        respLogin.headers["Set-Cookie"], "BNI_BARRACUDA_LB_COOKIE=", "; Path=/; HttpOnly")
    # print(cookieBarracuda_LogIn)

    viewstate_LogIn = extraer_texto(
        respLogin.text, 'id="j_id1:javax.faces.ViewState:0" value="', '" autocomplete="off"')
    # print(viewstate_LogIn)

    payload_Found = 'frmLogin=frmLogin&usuario=' + USUARIO + '&clave=' + CLAVE + \
        '&j_idt18=Ingresar&javax.faces.ViewState=' + \
        urllib.parse.quote(viewstate_LogIn, safe="")

    # print(payload_Found)

    headers_Found = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID=' + session_LogIn + '; BNI_BARRACUDA_LB_COOKIE=' + cookieBarracuda_LogIn,
        'Origin': COM_URL_BASE_CLOCATOR,
        'Referer': COM_URL_LOGIN,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    respFound = requests.request(
        "POST", COM_URL_FOUND + session_LogIn, headers=headers_Found, data=payload_Found)
    # print(respFound.text)

    payload_Main = {}

    headers_Main = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=' + session_LogIn + '; BNI_BARRACUDA_LB_COOKIE=' + cookieBarracuda_LogIn,
        'Referer': COM_URL_LOGIN,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    respMain = requests.request(
        "GET", COM_URL_MAIN, headers=headers_Main, data=payload_Main)

    # print(respMain.text)

    viewstate_Main = extraer_texto(
        respMain.text, 'id="j_id1:javax.faces.ViewState:0" value="', '" autocomplete="off"')
    # print(viewstate_Main)

    payload_prePopUpReporte = "javax.faces.partial.ajax=true&javax.faces.source=j_idt104%3AfnOpenItemMenu&javax.faces.partial.execute=%40all&j_idt104%3AfnOpenItemMenu=j_idt104%3AfnOpenItemMenu&pFuncionalidadId=437&pPadreId=8&pIrPagina=http%3A%2F%2Fclreportes.comsatel.com.pe%2FCLReporte%2F&j_idt104=j_idt104&javax.faces.ViewState=" + \
        urllib.parse.quote(viewstate_Main, safe="")

    headers_prePopUpReporte = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=' + session_LogIn + '; BNI_BARRACUDA_LB_COOKIE=' + cookieBarracuda_LogIn,
        'Faces-Request': 'partial/ajax',
        'Origin': COM_URL_BASE_CLOCATOR,
        'Referer': COM_URL_MAIN,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    respprePopUpReporte = requests.request(
        "POST", COM_URL_MAIN, headers=headers_prePopUpReporte, data=payload_prePopUpReporte)

    # print(respprePopUpReporte.headers)

    cookie_prePopUpReporte = extraer_texto(
        respprePopUpReporte.headers["Set-Cookie"], "", '; Domain')
    # Se necesita todo el session de Set-Cookie
    # print(cookie_prePopUpReporte)

    payload_CLReporte = {}

    headers_CLReporte = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': cookie_prePopUpReporte,
        'Referer': COM_URL_BASE_CLOCATOR,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    respCLReporte = requests.request(
        "GET", COM_URL_CLREPORTE, headers=headers_CLReporte, data=payload_CLReporte)

    # print(respCLReporte.text)

    session_CLReporte = extraer_texto(
        respCLReporte.headers["Set-Cookie"], "JSESSIONID=", "; Path=/CL")
    # print(session_CLReporte)

    cookieBarracuda_CLReporte = extraer_texto(
        respCLReporte.headers["Set-Cookie"], "BNI_BARRACUDA_LB_COOKIE=", "; Path=/; HttpOnly")
    # print(cookieBarracuda_CLReporte)

    viewstate_CLReporte = extraer_texto(
        respCLReporte.text, 'id="j_id1:javax.faces.ViewState:0" value="', '" autocomplete="off"')
    # print(viewstate_CLReporte)

    payload_preReporte = "javax.faces.partial.ajax=true&javax.faces.source=frmSesionLogin%3Aj_idt9&javax.faces.partial.execute=%40all&frmSesionLogin%3Aj_idt9=frmSesionLogin%3Aj_idt9&frmSesionLogin=frmSesionLogin&javax.faces.ViewState=" + \
        urllib.parse.quote(viewstate_CLReporte, safe="")

    headers_preReporte = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Accept-Language': 'en',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=' + session_CLReporte + ";" + cookie_prePopUpReporte + '; BNI_BARRACUDA_LB_COOKIE=' + cookieBarracuda_CLReporte,
        'Faces-Request': 'partial/ajax',
        'Origin': COM_URL_BASE_CLREPORTES,
        'Referer': COM_URL_CLREPORTE,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    resppreReporte = requests.request(
        "POST", "http://clreportes.comsatel.com.pe/CLReporte/faces/index.xhtml;jsessionid=" +
        session_CLReporte, headers=headers_preReporte, data=payload_preReporte)

    payload_ventanaReporte = {}
    headers_ventanaReporte = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=' + session_CLReporte + '; BNI_BARRACUDA_LB_COOKIE=' + cookieBarracuda_CLReporte,
        'Referer': COM_URL_CLREPORTE,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    respventanaReporte = requests.request(
        "GET", COM_URL_VEHICULOSINREPORTAR, headers=headers_ventanaReporte, data=payload_ventanaReporte)

    # Aquí debe decir "No cuenta con registros."

    # print(respventanaReporte.text)

    payload_clickDetalle = "javax.faces.partial.ajax=true&javax.faces.source=frmListar%3AchkDetalle&javax.faces.partial.execute=frmListar%3AchkDetalle&javax.faces.partial.render=frmListar%3AdtVehiculosSinReportar&javax.faces.behavior.event=valueChange&javax.faces.partial.event=change&frmListar=frmListar&frmListar%3AchkDetalle_input=on&frmListar%3AdtVehiculosSinReportar_selection=&javax.faces.ViewState=" + \
        urllib.parse.quote(viewstate_CLReporte, safe="")

    headers_clickDetalle = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=' + session_CLReporte + '; BNI_BARRACUDA_LB_COOKIE=' + cookieBarracuda_CLReporte,
        'Faces-Request': 'partial/ajax',
        'Origin': COM_URL_BASE_CLREPORTES,
        'Referer': COM_URL_VEHICULOSINREPORTAR,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    respclickDetalle = requests.request(
        "POST", COM_URL_VEHICULOSINREPORTAR, headers=headers_clickDetalle, data=payload_clickDetalle)

    # Busco con 0 horas desde que reportaron por última vez; es decir, todos
    payload_clickBuscar = 'cBusqueda%3AfrmBusquedaAvanzada=cBusqueda%3AfrmBusquedaAvanzada&cBusqueda%3AtxtPlaca=&cBusqueda%3AtxtNroMotor=&cBusqueda%3AtxtCodigoExterno=&cBusqueda%3AtxtDireccion=&cBusqueda%3AtxtVelocidad=&cBusqueda%3AcboIgnition=&cBusqueda%3AtxtOdometro=&cBusqueda%3AtxtNroSatelite=&cBusqueda%3AtxtTemperatura=&cBusqueda%3AsprTiempoSinReportar_input=0&cBusqueda%3AcboEstadoLoc=&cBusqueda%3AcboCompania=0&cBusqueda%3AcboFlota=0&cBusqueda%3AcboSubFlota=&javax.faces.ViewState=' + \
        urllib.parse.quote(viewstate_CLReporte, safe="") + \
        '&cBusqueda%3AfrmBusquedaAvanzada%3AbtnBuscar=cBusqueda%3AfrmBusquedaAvanzada%3AbtnBuscar'

    headers_clickBuscar = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID=' + session_CLReporte + '; BNI_BARRACUDA_LB_COOKIE=' + cookieBarracuda_CLReporte,
        'Origin': COM_URL_BASE_CLREPORTES,
        'Referer': COM_URL_VEHICULOSINREPORTAR,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    respclickBuscar = requests.request(
        "POST", COM_URL_VEHICULOSINREPORTAR, headers=headers_clickBuscar, data=payload_clickBuscar)

    # print(respclickBuscar.text)

    viewstate_clickBuscar = extraer_texto(
        respclickBuscar.text, 'id="j_id1:javax.faces.ViewState:0" value="', '" autocomplete="off"')
    print(viewstate_clickBuscar)

    payload_PopUpExcel = "javax.faces.partial.ajax=true&javax.faces.source=frmListar%3AbtnExportar&javax.faces.partial.execute=%40all&frmListar%3AbtnExportar=frmListar%3AbtnExportar&frmListar=frmListar&frmListar%3AchkDetalle_input=on&frmListar%3AdtVehiculosSinReportar_selection=&javax.faces.ViewState=" + \
        urllib.parse.quote(viewstate_clickBuscar, safe="")

    headers_PopUpExcel = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=' + session_CLReporte + '; BNI_BARRACUDA_LB_COOKIE=' + cookieBarracuda_CLReporte,
        'Faces-Request': 'partial/ajax',
        'Origin': COM_URL_BASE_CLREPORTES,
        'Referer': COM_URL_VEHICULOSINREPORTAR,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    # respPopUpExcel = requests.request(
    #    "POST", COM_URL_VEHICULOSINREPORTAR, headers=headers_PopUpExcel, data=payload_PopUpExcel)

    payload_DescargarExcel = 'exportarVehiculosSinReportar%3AfrmExportar=exportarVehiculosSinReportar%3AfrmExportar&javax.faces.ViewState=' + \
        urllib.parse.quote(viewstate_CLReporte, safe="") + \
        '&exportarVehiculosSinReportar%3AfrmExportar%3Aj_idt183=exportarVehiculosSinReportar%3AfrmExportar%3Aj_idt183'

    headers_DescargarExcel = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID=' + session_CLReporte + '; BNI_BARRACUDA_LB_COOKIE=' + cookieBarracuda_CLReporte,
        'Origin': COM_URL_BASE_CLREPORTES,
        'Referer': COM_URL_VEHICULOSINREPORTAR,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    fecha_nombrearchivo = datetime.today().strftime("%d%m%Y")
    nombreArchivo_Comsatel_local = "Comsatel_Excel_Python_" + \
        fecha_nombrearchivo + ".xlsx"
    nombreArchivo_Comsatel_lambda = "/tmp/Comsatel_Excel_Python_" + \
        fecha_nombrearchivo + ".xlsx"
    respDescargaExcel = requests.request(
        "POST", COM_URL_VEHICULOSINREPORTAR, headers=headers_DescargarExcel, data=payload_DescargarExcel)
    open(nombreArchivo_Comsatel_local, "wb").write(respDescargaExcel.content)

    # Manipulación
    POLY_TALLER_MOLINA = Polygon([(-12.071496, -76.955457), (-12.071008, -76.954843),
                                  (-12.070704, -76.953837), (-12.072157, -76.953322), (-12.0726576, -76.954998)])

    df = pd.read_excel(nombreArchivo_Comsatel_local, engine="openpyxl")
    # índice de filas. no se toma en cuenta a la columna
    # 1 placa
    # 2 ultimo reporte
    # 5 calle
    # 20 longitud
    # 21 latitud

    df = df[9:]
    # No se usa range df.shape, ya que no hay Unnameds
    df.columns = df.iloc[0]
    df = df[1:].iloc[:, [1, 4, 5, 11, 12]]
    df = df.rename(
        columns={df.columns[4]: "Fecha Ultima Localizacion", df.columns[5]: "Direccion"})
    df = df.drop(10)
    df = df.reset_index(drop=True)

    # 1 Placa
    # 4 Fecha última localización
    # 5 Dirección
    # 11 Latitud
    # 12 Longitud
    # Sí funciona a pesar del warning!
    # Sí funciona a pesar del warning!
    # Sí funciona a pesar del warning!
    # Sí funciona a pesar del warning!
    # Sí funciona a pesar del warning!
    # Sí funciona a pesar del warning!
    # Sí funciona a pesar del warning!
    # Sí funciona a pesar del warning!
    # Sí funciona a pesar del warning!

    # Sí funciona a pesar del warning!
    # Sí funciona a pesar del warning!
    # Sí funciona a pesar del warning!
    # Sí funciona a pesar del warning!
    # Sí funciona a pesar del warning!
    # Para usar polígono debe ser número y no string
    df["temp"] = df.Placa.str.len()  # Contar caracteres de columna Placa
    df = df[df.temp == 6]  # Me quedo con las filas en los que temp sea 6
    df["Latitud"] = df["Latitud"].astype(float)
    # Para usar polígono debe ser número y no string
    df["Longitud"] = df["Longitud"].astype(float)
    df["Alias"] = df["Placa"]
    df["Placa"] = df["Placa"].str[:3] + "-" + \
        df["Placa"].str[3:]  # Coloca guión a la placa
    df["Taller Molina"] = df.apply(lambda x: POLY_TALLER_MOLINA.contains(
        Point(x["Latitud"], x["Longitud"])), axis=1)
    df["Fecha Ultima Localizacion"] = df["Fecha Ultima Localizacion"].astype(
        str)
    df["temp_fecha"] = df["Fecha Ultima Localizacion"].str.len()
    df["temp_fecha"] = df["temp_fecha"].astype(np.int64)
    # print(df)
    df["Fecha"] = df.apply(
        lambda x: x["Fecha Ultima Localizacion"][0:10], axis=1)  # extrae la placa
    df["Hora"] = df.apply(
        lambda x: x["Fecha Ultima Localizacion"][11:x["temp_fecha"]-1], axis=1)  # extrae la placa
    df["Hora"] = df["Hora"].str[:-2]
    del df["temp_fecha"]  # elimina columna temporal
    del df["temp"]  # elimina columna temporal
    df["Proveedor"] = "Comsatel"
    comsatel_df = df
    # print(df_c)
    comsatel_csv_filename = hoy + "_comsatel.csv"
    comsatel_df.to_csv(comsatel_csv_filename, index=False)
    # Sí funciona a pesar del warning!
    os.remove(nombreArchivo_Comsatel_local)
    return comsatel_df
