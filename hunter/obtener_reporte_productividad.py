import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import pandas as pd
HUN_URL_BASE = "http://www.huntermonitoreoperu.com"
HUN_URL_PANEL = "http://190.223.20.13/reportes/admin_report.php?perfil=4&idusuario=93084&idsubusuario=0&Version=3"
HUN_URL_PRODUCTIVIDAD = "http://190.223.20.13/reportes/resumen_productividad.php"
HUN_URL_AJAXCONTROLLER = "http://190.223.20.13/reportes/inc/ajax_controller.php"
HUN_URL_SAVERANKING = "http://190.223.20.13/reportes/inc/saveRanking.php"
USUARIO = "20605414410"
CLAVE = "mb504"
TIPO_REPORTE = "productividad"


def juntar_codigos_placas(lista_codigos_placas):
    string_lista_codigos = ""
    for c in lista_codigos_placas:
        string_lista_codigos = string_lista_codigos + c + "%2C"
    # Eliminar últimos 3 caracteres
    string_lista_codigos = string_lista_codigos[:-3]
    return string_lista_codigos

# payload yyyymmdd


def fecha(delta):
    d = datetime.today() - timedelta(days=delta)
    fecha_yyyymmdd = d.strftime("%Y%m%d")
    fecha_ddmmyyyy = d.strftime("%d/%m/%Y")
    return fecha_yyyymmdd, fecha_ddmmyyyy


def ayer():
    d = datetime.today() - timedelta(days=1)
    d_p = d.strftime("%Y%m%d")
    d_df = d.strftime("%d/%m/%Y")
    return d_p, d_df


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    # empieza a buscar el fin a partir del inicio
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def convertir_hhmmss(hhmmss):
    if hhmmss == " :00" or hhmmss == "0":
        hora = 0
    else:
        # Obtener los 3 datos de hh:mm:ss
        h = extraer_texto(hhmmss, "", ":")
        # print(h)
        h = int(h)
        m = extraer_texto(hhmmss, ":", ":")
        # print(m)
        m = int(m)
        s = hhmmss[-2:]
        # print(s)
        s = int(s)
        hora = h + m/60 + s/3600
    return hora


def convertir_placa(alias):
    c = "-"
    pos_guion = alias.find(c)
    if pos_guion != -1:
        placa = alias[pos_guion-3:pos_guion+4]
    else:
        placa = alias
    return placa


def calcular_porcentaje_ralenti(duracion, duracion_ralenti):

    if (duracion_ralenti == 0):
        porcentaje_ralenti = 0
    else:
        porcentaje_ralenti = (
            duracion_ralenti/(duracion+duracion_ralenti))
    return porcentaje_ralenti


def limpiar_descripcion_vehiculo(descripcion_vehiculo):
    sin_comas = descripcion_vehiculo.replace(',', '')
    return sin_comas


def crear_csv_productividad(respuesta, fecha):

    lista_placa = []
    lista_descripcion_vehiculo = []
    lista_fecha = []
    lista_tipo_reporte = []
    lista_dias_usados = []
    lista_duracion = []
    lista_distancia = []
    lista_velocidad_maxima = []
    lista_duracion_ralenti = []
    # Esto se puede calcular directamente en el BI
    lista_porcentaje_ralenti = []

    doc = BeautifulSoup(respuesta, "html.parser")
    for t in doc.find_all(
            "table", {"id": "report"}):
        for tr in t.find_all("tr", {"class": "rows"}):
            td = tr.find_all("td")
            # print(td)
            placa = convertir_placa(td[0].text)
            lista_placa.append(placa)
            descripcion_vehiculo = limpiar_descripcion_vehiculo(td[0].text)
            lista_descripcion_vehiculo.append(descripcion_vehiculo)
            lista_fecha.append(fecha)
            lista_tipo_reporte.append(TIPO_REPORTE)
            lista_dias_usados.append(td[1].text)
            duracion = convertir_hhmmss(td[2].text)
            lista_duracion.append(duracion)
            lista_distancia.append(td[3].text)
            lista_velocidad_maxima.append(td[5].text)
            duracion_ralenti = convertir_hhmmss(td[12].text)
            lista_duracion_ralenti.append(duracion_ralenti)
            porcentaje_ralenti = calcular_porcentaje_ralenti(
                duracion, duracion_ralenti)
            lista_porcentaje_ralenti.append(porcentaje_ralenti)

    # print(temp)

    dict_productividad = {"placa": lista_placa,
                          "descripcion_vehiculo": lista_descripcion_vehiculo,
                          "fecha": lista_fecha,
                          "tipo_reporte": lista_tipo_reporte,
                          "dias_uso": lista_dias_usados,
                          "horas_movimiento": lista_duracion,
                          "distancia": lista_distancia,
                          "velocidad_maxima": lista_velocidad_maxima,
                          "horas_ralenti": lista_duracion_ralenti,
                          "porcentaje_ralenti": lista_porcentaje_ralenti ,
                          "proveedor":"Hunter"}
    productividad_df = pd.DataFrame(dict_productividad)
    #productividad_df_filename = "hunter_productividad.csv"
    #productividad_df.to_csv(productividad_df_filename, index=False)
    return productividad_df


def obtener_reporte_productividad(c, hora_reporte):

    payload_Panel = {}
    headers_Panel = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': HUN_URL_BASE,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    # response_Panel = requests.request(
    #     "GET", HUN_URL_PANEL, headers=headers_Panel, data=payload_Panel)

    payload_Categoriaperfil = "tipoTree=entidad&idusuario=93084&idsubusuario=0&idperfil=4"
    headers_Categoriaperfil = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://190.223.20.13',
        'Referer': HUN_URL_PANEL,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    # response_Categoriaperfil = requests.request(
    #     "POST", HUN_URL_PRODUCTIVIDAD, headers=headers_Categoriaperfil, data=payload_Categoriaperfil)

    payload_Ajaxcontroller = "opcion=listarConductor&idUsuario=93084"
    headers_Ajaxcontroller = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://190.223.20.13',
        'Referer': HUN_URL_PANEL,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    # response_Ajaxcontroller = requests.request(
    #     "POST", HUN_URL_AJAXCONTROLLER, headers=headers_Ajaxcontroller, data=payload_Ajaxcontroller)

    payload_Saveranking = "idu=93084&idri=IRA&idrt=RESUMEN+DE+PRODUCTIVIDAD+DE+MANEJO&idsi=NULL&idst=NULL"
    headers_Saveranking = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://190.223.20.13',
        'Referer': HUN_URL_PANEL,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    # response_Saveranking = requests.request(
    #     "POST", HUN_URL_SAVERANKING, headers=headers_Saveranking, data=payload_Saveranking)

    # Reporte: Resumen de Productividad de Manejo

    # 0: payload yyyymmdd
    # 1: dataframe dd/mm/yyyy
    #fecha_payload = fecha(hora_reporte)
    if hora_reporte == "Ayer":
        fecha_payload = fecha(1)  # dd/mm/yyyy
    elif hora_reporte == "Hoy":
        fecha_payload = fecha(0)  # dd/mm/yyyy
    string_codigos_placas_payload = juntar_codigos_placas(c)
    payload_Reporteproductividad = 'u=93084&v='+string_codigos_placas_payload + \
        '&i=' + fecha_payload[0] + '&f=' + fecha_payload[0] + '&vv=&cl='+CLAVE + \
        '&ts=RNT&e='+USUARIO+'**EG*01&version=undefined'
    headers_Reporteproductividad = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://190.223.20.13',
        'Referer': HUN_URL_PANEL,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    response_Reporteproductividad = requests.request(
        "POST", HUN_URL_PRODUCTIVIDAD, headers=headers_Reporteproductividad, data=payload_Reporteproductividad)

    df = crear_csv_productividad(
        response_Reporteproductividad.text, fecha_payload[1])
    return df
