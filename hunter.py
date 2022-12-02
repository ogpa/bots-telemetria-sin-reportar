import requests
import urllib
from datetime import datetime
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import pandas as pd
import numpy as np
import os
from asignar_region import asignar_region
HUN_URL_LOGIN = "http://www.huntermonitoreoperu.com/GeoV3.3/LoginV3.aspx"
HUN_URL_MAINHTML = "http://www.huntermonitoreoperu.com/GeoV3.3/Paginas/Main.html?r="
HUN_URL_MAIN36 = "http://www.huntermonitoreoperu.com/GeoV3.3/Paginas/Main36.aspx"
HUN_URL_ESTADOFLOTA = "http://www.huntermonitoreoperu.com/GeoV3.3/Paginas/EstadoFlota/Estado.aspx?TIME="
USUARIO = "20605414410"
CLAVE = "mb504"
INICIO_GRESTADOFLOTA = "{&quot;columnsExpandedState&quot;:{&quot;0&quot;:true,&quot;1&quot;:true,&quot;2&quot;:true,&quot;3&quot;:false,&quot;4&quot;:true,&quot;5&quot;:true,&quot;6&quot;:true,&quot;7&quot;:true,&quot;8&quot;:true,&quot;9&quot;:true,&quot;10&quot;:true,&quot;11&quot;:true,&quot;12&quot;:true,&quot;13&quot;:true,&quot;14&quot;:true,&quot;15&quot;:true,&quot;16&quot;:false,&quot;17&quot;:true,&quot;18&quot;:true,&quot;19&quot;:true,&quot;20&quot;:true,&quot;21&quot;:true,&quot;22&quot;:false,&quot;23&quot;:true,&quot;24&quot;:true,&quot;25&quot;:true,&quot;26&quot;:true,&quot;27&quot;:true,&quot;28&quot;:true,&quot;29&quot;:false,&quot;30&quot;:true,&quot;31&quot;:true,&quot;32&quot;:true,&quot;33&quot;:false,&quot;34&quot;:true,&quot;35&quot;:true,&quot;36&quot;:true,&quot;37&quot;:true,&quot;38&quot;:true,&quot;39&quot;:true,&quot;40&quot;:false,&quot;41&quot;:true,&quot;42&quot;:true,&quot;43&quot;:true,&quot;44&quot;:true,&quot;45&quot;:true,&quot;46&quot;:true,&quot;47&quot;:true,&quot;48&quot;:true,&quot;49&quot;:true,&quot;50&quot;:true,&quot;51&quot;:true,&quot;52&quot;:true,&quot;53&quot;:true,&quot;54&quot;:true,&quot;55&quot;:true,&quot;56&quot;:false,&quot;57&quot;:true,&quot;58&quot;:true,&quot;59&quot;:true,&quot;60&quot;:true,&quot;61&quot;:true,&quot;62&quot;:true,&quot;63&quot;:true,&quot;64&quot;:true,&quot;65&quot;:true,&quot;66&quot;:true,&quot;67&quot;:true,&quot;68&quot;:true,&quot;69&quot;:true,&quot;70&quot;:true,&quot;71&quot;:true,&quot;72&quot;:true,&quot;73&quot;:true,&quot;74&quot;:true,&quot;75&quot;:true,&quot;76&quot;:true,&quot;77&quot;:false},&quot;keys&quot;:[&quot;4634524408&quot;,&quot;4635223147&quot;,&quot;4635224310&quot;,&quot;4634526626&quot;],&quot;callbackState&quot;:&quot;"
FIN_GRESTADOFLOTA = "&quot;,&quot;scrollState&quot;:null,&quot;selection&quot;:&quot;&quot;,&quot;toolbar&quot;:null}"

POLY_TALLER_MOLINA = Polygon([(-12.071496, -76.955457), (-12.071008, -76.954843),
                              (-12.070704, -76.953837), (-12.072157, -76.953322), (-12.0726576, -76.954998)])


def scan_hunter(hoy):
    respLogin = requests.request("GET", HUN_URL_LOGIN)

    def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
        ini = textomaster.find(ini_cabecera)
        # empieza a buscar el fin a partir del inicio
        fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
        # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
        texto = textomaster[ini+len(ini_cabecera):fin]
        return texto

    cookie_LogIn = extraer_texto(
        respLogin.headers["Set-Cookie"], "ASP.NET_SessionId=", "; path=/;")
    # print(cookie_LogIn)

    viewstate_LogIn = extraer_texto(
        respLogin.text, 'id="__VIEWSTATE" value="', '"')
    # print(viewstate_LogIn)

    viewstategenerator_LogIn = extraer_texto(
        respLogin.text, 'id="__VIEWSTATEGENERATOR" value="', '"')
    # print(viewstategenerator_LogIn)

    eventvalidation_LogIn = extraer_texto(
        respLogin.text, 'id="__EVENTVALIDATION" value="', '"')
    # print(eventvalidation_LogIn)

    payload_LogInV3 = '__EVENTTARGET=btningresar&__EVENTARGUMENT=&__VIEWSTATE=' + urllib.parse.quote(viewstate_LogIn, safe="") + '&__VIEWSTATEGENERATOR=' + viewstategenerator_LogIn + '&__EVENTVALIDATION=' + urllib.parse.quote(eventvalidation_LogIn, safe="") + '&txusuario=' + USUARIO + '&txclave=' + CLAVE + \
        '&hdintentos=1&vnRegistroWebState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&vnReclamosState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&vnRestablecerState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&bNoticiasState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A39%3A374%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&vnAgenciasState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&DXScript=1_11%2C1_252%2C1_12%2C1_23%2C1_64%2C1_14%2C1_15%2C1_17%2C1_41&DXCss=0_2771%2C1_68%2C1_69%2C0_2776'

    headers_LogInV3 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': "ASP.NET_SessionId=" + cookie_LogIn,
        'Origin': 'http://www.huntermonitoreoperu.com',
        'Referer': HUN_URL_LOGIN,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    respLoginV3 = requests.request(
        "POST", HUN_URL_LOGIN, headers=headers_LogInV3, data=payload_LogInV3)

    # print(respLoginV3.text)

    headers_Main36 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': "ASP.NET_SessionId=" + cookie_LogIn,
        'Origin': 'http://www.huntermonitoreoperu.com',
        'Referer': HUN_URL_MAINHTML,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    respMain36 = requests.request(
        "GET", HUN_URL_MAIN36, headers=headers_Main36)

    # print(respMain36.text)
    time_Main36 = extraer_texto(
        respMain36.text, 'id="hdwuid" value="', '"')

    # print(time_Main36)

    headers_EstadoFlota = {
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en",
        "Connection": "keep-alive",
        "Cookie": "ASP.NET_SessionId=" + cookie_LogIn,
        "Referer": HUN_URL_MAIN36,
        "Upgrade-Insecure-Requests": "1",
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }

    respEstadoFlota = requests.request(
        "GET", HUN_URL_ESTADOFLOTA + time_Main36, headers=headers_EstadoFlota)

    time_EstadoFlota = extraer_texto(
        respEstadoFlota.text, 'id="hdwuid" value="', '"')

    viewstate_EstadoFlota = extraer_texto(
        respEstadoFlota.text, 'id="__VIEWSTATE" value="', '"')

    viewstategenerator_EstadoFlota = extraer_texto(
        respEstadoFlota.text, 'id="__VIEWSTATEGENERATOR" value="', '"')

    eventvalidation_EstadoFlota = extraer_texto(
        respEstadoFlota.text, 'id="__EVENTVALIDATION" value="', '"')

    callbackstate_EstadoFlota = extraer_texto(
        respEstadoFlota.text, "],'callbackState':'", "','scrollState':")

    # print(callbackstate_EstadoFlota)

    payload_DescargarExcel = '__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=' + urllib.parse.quote(viewstate_EstadoFlota, safe="") + '&__VIEWSTATEGENERATOR=' + viewstategenerator_EstadoFlota + '&__EVENTVALIDATION=' + urllib.parse.quote(eventvalidation_EstadoFlota, safe="") + '&imgExcel.x=4&imgExcel.y=17&kmsResumen=%7B%26quot%3BcallbackState%26quot%3B%3A%26quot%3B%26quot%3B%7D&grdEstadoFlota=' + urllib.parse.quote(INICIO_GRESTADOFLOTA + callbackstate_EstadoFlota + FIN_GRESTADOFLOTA, safe="") + \
        '&grdEstadoFlota%24DXSE%24State=%7B%26quot%3BrawValue%26quot%3B%3A%26quot%3B%26quot%3B%7D&grdEstadoFlota%24DXSE=&grdEstadoFlota%24DXHFPState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&hdboton=&DXScript=1_11%2C1_252%2C1_12%2C1_23%2C1_64%2C1_14%2C1_15%2C1_49%2C10_0%2C10_1%2C10_2%2C10_3%2C10_4%2C1_21%2C1_22%2C1_19%2C1_213%2C1_224%2C1_225%2C1_212%2C1_214%2C1_222%2C1_211%2C1_241%2C1_242%2C1_243%2C1_244%2C1_245%2C1_246%2C1_183%2C1_184%2C1_182%2C1_17%2C1_41%2C1_39&DXCss=1_68%2C1_69%2C0_629%2C0_5094%2C0_2754%2C0_2771%2C0_2758%2C0_2776%2C1_210%2C0_2685%2C1_209%2C0_2690'

    headers_DescargarExcel = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': "ASP.NET_SessionId=" + cookie_LogIn,
        'Origin': 'http://www.huntermonitoreoperu.com',
        'Referer': HUN_URL_ESTADOFLOTA + time_Main36,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    fecha_nombrearchivo = datetime.today().strftime("%d%m%Y")
    nombreArchivo_Hunter_local = "Hunter_Excel_Python_" + fecha_nombrearchivo + ".xlsx"
    nombreArchivo_Hunter_lambda = "/tmp/Hunter_Excel_Python_" + \
        fecha_nombrearchivo + ".xlsx"

    respDescargaExcel = requests.request(
        "POST", HUN_URL_ESTADOFLOTA + time_Main36, headers=headers_DescargarExcel, data=payload_DescargarExcel)
    open(nombreArchivo_Hunter_local, "wb").write(respDescargaExcel.content)

    # Manipulación

    #POLY_TALLER_MOLINA = Polygon([(-12.071496, -76.955457), (-12.071008, -76.954843),(-12.070704, -76.953837), (-12.072157, -76.953322), (-12.0726576, -76.954998)])

    #RUTA_EXCEL_HUNTER = "Excel_Hunter_Python.xlsx"

    # file_path = Path(RUTA_EXCEL_HUNTER)
    # file_extension = file_path.suffix.lower()[1:]

    # if file_extension == 'xlsx':
    #     df = pd.read_excel(file.read(), engine='openpyxl')
    # elif file_extension == 'xls':
    #     df = pd.read_excel(file.read())
    # elif file_extension == 'csv':
    #     df = pd.read_csv(file.read())
    # else:
    #     raise Exception("File not supported")

    df = pd.read_excel(nombreArchivo_Hunter_local)  # df = data frame
    # índice de filas. no se toma en cuenta a la columna
    # 1 placa
    # 2 ultimo reporte
    # 5 calle
    # 20 longitud
    # 21 latitud
    # iloc[1:, 1:] =  Selecciona todo desde la segunda fila y segunda columna
    # T = Invierte la orientación de la data
    # iloc[:, [0, 1, 4, 19, 20]] = Selecciona las columnas 0,1,4,19,20

    # print(range(df.shape[1]))  # elimina primera fila de Unnamed
    # Asigna nueva fila de headers. Sirve para borrar los Unnamed
    df.columns = range(df.shape[1])
    df = df.iloc[1:, 1:].T.iloc[:, [0, 1, 20, 19, 4]]
    df.columns = df.iloc[0]  # los headers serán la primera fila de datos
    # extraigo todo excepto la primera fila, porque se repetiría la fila de headers
    df = df[1:]
    df = df.drop_duplicates()
    # posicion del caracter "-" en entero
    df["temp"] = df.Alias.str.find("-")
    df = df.dropna(subset=["temp"])  # elimina NaN de la columna temp
    # convierte flota64 a int64 de columna temp
    df["temp"] = df["temp"].astype(np.int64)

    df["Latitud"] = df["Latitud"].astype(float)
    df["Longitud"] = df["Longitud"].astype(float)
    df["Placa"] = df.apply(lambda x: x["Alias"][x["temp"] -
                                                3:x["temp"]+4], axis=1)  # extrae la placa
    del df["temp"]  # elimina columna temporal
    df["Taller Molina"] = df.apply(lambda x: POLY_TALLER_MOLINA.contains(
        Point(x["Latitud"], x["Longitud"])), axis=1)
    df["Region"] = df.apply(lambda x: asignar_region(
        x["Latitud"], x["Longitud"]), axis=1)
    # Le cambio el nombre para que sea igual que el de Comsatel
    df = df.rename(
        columns={df.columns[1]: "Fecha Ultima Localizacion", df.columns[4]: "Direccion"})
    # print(df.columns)
    # Contar caracteres de columa 'Ultimo reporte

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
    df["Proveedor"] = "Hunter"
    df = df.drop_duplicates(subset="Placa")
    hunter_df = df
    # print(df_h)
    # print(hunter_df.iloc[195])  # Para veirficar que el polígono está funcionando

    #print("El programa tomó %s segundos en ejecutarse." %round(time.time() - start_time, 1))

    # UNIR

    #s3.meta.client.upload_file(nombre_archivo_final_s3, S3_BUCKET_NAME, nombre_archivo_final)
    hunter_csv_filename = hoy + "_hunter.csv"
    hunter_df.to_csv(hunter_csv_filename, index=False)
    os.remove(nombreArchivo_Hunter_local)
    return hunter_df
