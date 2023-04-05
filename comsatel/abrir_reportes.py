import requests
import urllib
from comsatel.funciones_comsatel.extraer_datos_session import extraer_datos_session
CABECERA_SESSION = 'JSESSIONID='
CABECERA_COOKIE_BARRACUDA = 'BNI_BARRACUDA_LB_COOKIE='
COM_URL_BASE_CLOCATOR = "http://clocatorplus.comsatel.com.pe"
COM_URL_MAIN = "http://clocatorplus.comsatel.com.pe/CL/faces/page/main.xhtml"
COM_URL_CLREPORTE = "http://clreportes.comsatel.com.pe/CLReporte/"
COM_URL_BASE_CLREPORTES = "http://clreportes.comsatel.com.pe"


def abrir_reportes(vs_main, s_login, c_login):  # Viewstate

    payload_Pre_PopUpReporte = "javax.faces.partial.ajax=true&javax.faces.source=j_idt104%3AfnOpenItemMenu&javax.faces.partial.execute=%40all&j_idt104%3AfnOpenItemMenu=j_idt104%3AfnOpenItemMenu&pFuncionalidadId=119&pPadreId=8&pIrPagina=http%3A%2F%2Fclreportes.comsatel.com.pe%2FCLReporte%2F&j_idt104=j_idt104&javax.faces.ViewState=" + \
        urllib.parse.quote(vs_main, safe="")

    headers_Pre_PopUpReporte = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': CABECERA_SESSION + s_login + '; ' + CABECERA_COOKIE_BARRACUDA + c_login,
        'Faces-Request': 'partial/ajax',
        'Origin': COM_URL_BASE_CLOCATOR,
        'Referer': COM_URL_MAIN,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response_Pre_PopUpReporte = requests.request(
        "POST", COM_URL_MAIN, headers=headers_Pre_PopUpReporte, data=payload_Pre_PopUpReporte)

    d_Pre_PopUpReporte = extraer_datos_session(response_Pre_PopUpReporte)
    c_Pre_PopUpReporte = d_Pre_PopUpReporte[3]

    payload_CLReporte = {}

    headers_CLReporte = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': c_Pre_PopUpReporte,
        'Referer': COM_URL_BASE_CLOCATOR,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    response_CLReporte = requests.request(
        "GET", COM_URL_CLREPORTE, headers=headers_CLReporte, data=payload_CLReporte)

    d_CLReporte = extraer_datos_session(response_CLReporte)

    s_CLReporte = d_CLReporte[0]  # Session
    c_b_CLReporte = d_CLReporte[1]  # Cookie barracuda
    vs_CLReporte = d_CLReporte[2]  # Viewstate

    payload_Pre_Reporte = "javax.faces.partial.ajax=true&javax.faces.source=frmSesionLogin%3Aj_idt9&javax.faces.partial.execute=%40all&frmSesionLogin%3Aj_idt9=frmSesionLogin%3Aj_idt9&frmSesionLogin=frmSesionLogin&javax.faces.ViewState=" + \
        urllib.parse.quote(vs_CLReporte, safe="")

    headers_Pre_Reporte = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Accept-Language': 'en',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': CABECERA_SESSION + s_CLReporte + ";" + c_Pre_PopUpReporte + '; ' + CABECERA_COOKIE_BARRACUDA + c_b_CLReporte,
        'Faces-Request': 'partial/ajax',
        'Origin': COM_URL_BASE_CLREPORTES,
        'Referer': COM_URL_CLREPORTE,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response_Pre_Reporte = requests.request(
        "POST", "http://clreportes.comsatel.com.pe/CLReporte/faces/index.xhtml;jsessionid=" +
        s_CLReporte, headers=headers_Pre_Reporte, data=payload_Pre_Reporte)

    return s_CLReporte, c_b_CLReporte, vs_CLReporte
