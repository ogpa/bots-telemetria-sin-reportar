import requests
import urllib
from datetime import datetime, timedelta
from comsatel.funciones_comsatel.extraer_datos_session import extraer_datos_session
COM_URL_CLREPORTE = "http://clreportes.comsatel.com.pe/CLReporte/"
CABECERA_SESSION = 'JSESSIONID='
CABECERA_COOKIE_BARRACUDA = 'BNI_BARRACUDA_LB_COOKIE='
COM_URL_CONSOLIDADO = "http://clreportes.comsatel.com.pe/CLReporte/faces/page/consolidado/consolidadoListar.xhtml"
COM_URL_BASE_CLREPORTES = "http://clreportes.comsatel.com.pe"


def fecha(delta):
    d = datetime.today() - timedelta(days=delta, hours=5)
    fecha_ddmmyyyy = d.strftime("%d/%m/%Y")
    return fecha_ddmmyyyy


def obtener_reporte_consolidado(a, hora_reporte):  # Datos de abrir_reportes
    # 0 -> s_CLReporte
    # 1 -> c_b_CLReporte
    # 2 -> vs_CLReporte
    s_CLReporte = a[0]
    c_b_CLReporte = a[1]
    vs_CLReporte = a[2]
    payload_Ventana_Reporte = {}
    headers_Ventana_Reporte = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en',
        'Connection': 'keep-alive',
        'Cookie': CABECERA_SESSION + s_CLReporte + '; ' + CABECERA_COOKIE_BARRACUDA + c_b_CLReporte,
        'Referer': COM_URL_CLREPORTE,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    response_Ventana_Reporte = requests.request(
        "GET", COM_URL_CONSOLIDADO, headers=headers_Ventana_Reporte, data=payload_Ventana_Reporte)

    # Aquí debe decir "No cuenta con registros" o "No records found"
    # print(response_Ventana_Reporte.text)
    d_Ventana_Reporte = extraer_datos_session(response_Ventana_Reporte)

    s_Ventana_Reporte = d_Ventana_Reporte[0]  # Session
    c_b_Ventana_Reporte = d_Ventana_Reporte[1]  # Cookie barracuda
    vs_Ventana_Reporte = d_Ventana_Reporte[2]  # Viewstate

    payload_Formato_Horas = "javax.faces.partial.ajax=true&javax.faces.source=frmListar%3Aj_idt84&javax.faces.partial.execute=frmListar%3Aj_idt84&javax.faces.behavior.event=change&javax.faces.partial.event=change&frmListar=frmListar&frmListar%3Aj_idt84=on&javax.faces.ViewState=" + \
        urllib.parse.quote(vs_Ventana_Reporte, safe="")
    headers_Formato_Horas = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': CABECERA_SESSION + s_CLReporte + '; ' + CABECERA_COOKIE_BARRACUDA + c_b_CLReporte,
        'Faces-Request': 'partial/ajax',
        'Origin': COM_URL_BASE_CLREPORTES,
        'Referer': COM_URL_CONSOLIDADO,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response_Formato_Horas = requests.request(
        "POST", COM_URL_CONSOLIDADO, headers=headers_Formato_Horas, data=payload_Formato_Horas)

    payload_Campos_Adicionales = "javax.faces.partial.ajax=true&javax.faces.source=frmListar%3Aj_idt86&javax.faces.partial.execute=frmListar%3Aj_idt86&javax.faces.partial.render=frmListar&javax.faces.behavior.event=change&javax.faces.partial.event=change&frmListar=frmListar&frmListar%3Aj_idt84=on&frmListar%3Aj_idt86=on&javax.faces.ViewState=" + \
        urllib.parse.quote(vs_Ventana_Reporte, safe="")
    headers_Campos_Adicionales = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': CABECERA_SESSION + s_CLReporte + '; ' + CABECERA_COOKIE_BARRACUDA + c_b_CLReporte,
        'Faces-Request': 'partial/ajax',
        'Origin': COM_URL_BASE_CLREPORTES,
        'Referer': COM_URL_CONSOLIDADO,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response_Campos_Adicionales = requests.request(
        "POST", COM_URL_CONSOLIDADO, headers=headers_Campos_Adicionales, data=payload_Campos_Adicionales)

    # 0: payload yyyymmdd
    # 1: dataframe dd/mm/yyyy
    if hora_reporte == "Ayer":
        fecha_payload = fecha(1)  # dd/mm/yyyy
    elif hora_reporte == "Hoy":
        fecha_payload = fecha(0)  # dd/mm/yyyy

    #print(urllib.parse.quote(fecha_ayer[1], safe=""))
    payload_Found_Click_Buscar = 'j_idt45%3AfrmBusquedaAvanzada=j_idt45%3AfrmBusquedaAvanzada&j_idt45%3AtxtFechaInicioA_input=' + urllib.parse.quote(fecha_payload, safe="") + '&j_idt45%3AtxtFechaFinA_input=' + urllib.parse.quote(
        fecha_payload, safe="") + '&j_idt45%3AtxtPlacaA=&j_idt45%3AtxtCodigoExternoA=&j_idt45%3AcboCompania=0&j_idt45%3AtxtNroMotorA=&j_idt45%3AcboFlota=0&j_idt45%3AcboSubFlota=0&javax.faces.ViewState=' + urllib.parse.quote(vs_Ventana_Reporte, safe="") + '&j_idt45%3AfrmBusquedaAvanzada%3AbtnBuscar=j_idt45%3AfrmBusquedaAvanzada%3AbtnBuscar'
    headers_Found_Click_Buscar = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': CABECERA_SESSION + s_CLReporte + '; ' + CABECERA_COOKIE_BARRACUDA + c_b_CLReporte,
        'Origin': COM_URL_BASE_CLREPORTES,
        'Referer': COM_URL_CONSOLIDADO,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    response_Found_Click_Buscar = requests.request(
        "POST", COM_URL_CONSOLIDADO, headers=headers_Found_Click_Buscar, data=payload_Found_Click_Buscar)
    # print(response_Found_Click_Buscar.text)

    payload_Click_Buscar = {}

    headers_Click_Buscar = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': CABECERA_SESSION + s_CLReporte + '; ' + CABECERA_COOKIE_BARRACUDA + c_b_CLReporte,
        'Referer': COM_URL_CONSOLIDADO,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response_Click_Buscar = requests.request(
        "GET", COM_URL_CONSOLIDADO, headers=headers_Click_Buscar, data=payload_Click_Buscar)
    # print(response_Click_Buscar.text)

    d_Click_Buscar = extraer_datos_session(response_Click_Buscar)

    vs_Click_Buscar = d_Click_Buscar[2]  # Viewstate

    payload_PopUpExcel = "javax.faces.partial.ajax=true&javax.faces.source=frmListar%3Aj_idt145&javax.faces.partial.execute=%40all&frmListar%3Aj_idt145=frmListar%3Aj_idt145&frmListar=frmListar&frmListar%3Aj_idt84=on&frmListar%3Aj_idt86=on&javax.faces.ViewState=" + \
        urllib.parse.quote(vs_Click_Buscar, safe="")

    headers_PopUpExcel = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9,es;q=0.8,it;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': CABECERA_SESSION + s_CLReporte + '; ' + CABECERA_COOKIE_BARRACUDA + c_b_CLReporte,
        'Faces-Request': 'partial/ajax',
        'Origin': COM_URL_BASE_CLREPORTES,
        'Referer': COM_URL_CONSOLIDADO,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response_PopUpExcel = requests.request(
        "POST", COM_URL_CONSOLIDADO, headers=headers_PopUpExcel, data=payload_PopUpExcel)

    payload_DescargarExcel = 'j_idt156=j_idt156&javax.faces.ViewState=' + \
        urllib.parse.quote(vs_Click_Buscar, safe="") + \
        '&j_idt156%3Aj_idt158=j_idt156%3Aj_idt158'

    headers_DescargarExcel = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': CABECERA_SESSION + s_CLReporte + '; ' + CABECERA_COOKIE_BARRACUDA + c_b_CLReporte,
        'Origin': COM_URL_BASE_CLREPORTES,
        'Referer': COM_URL_CONSOLIDADO,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    nombreArchivo_Comsatel_local = hora_reporte + "_Consolidado_Comsatel.xlsx"

    response_DescargaExcel = requests.request(
        "POST", COM_URL_CONSOLIDADO, headers=headers_DescargarExcel, data=payload_DescargarExcel)

    open(nombreArchivo_Comsatel_local, "wb").write(
        response_DescargaExcel.content)

    return nombreArchivo_Comsatel_local
