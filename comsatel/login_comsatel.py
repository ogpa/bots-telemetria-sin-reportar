import requests
import urllib
from comsatel.funciones_comsatel.extraer_datos_session import extraer_datos_session
COM_URL_BASE_CLOCATOR = "http://clocatorplus.comsatel.com.pe"
COM_URL_LOGIN = "http://clocatorplus.comsatel.com.pe/CL/faces/seguridad/login.xhtml"
COM_URL_FOUND = "http://clocatorplus.comsatel.com.pe/CL/faces/seguridad/login.xhtml;jsessionid="
COM_URL_MAIN = "http://clocatorplus.comsatel.com.pe/CL/faces/page/main.xhtml"
COM_URL_CLREPORTE = "http://clreportes.comsatel.com.pe/CLReporte/"
COM_URL_VEHICULOSINREPORTAR = "http://clreportes.comsatel.com.pe/CLReporte/faces/page/vehiculossinreportar/vehiculosSinReportarListar.xhtml"
USUARIO = "DPIZARRO"
CLAVE = "JDP9L9HKEYiQaXH"
CABECERA_SESSION = 'JSESSIONID='
CABECERA_COOKIE_BARRACUDA = 'BNI_BARRACUDA_LB_COOKIE='


def login_comsatel():
    response_Login = requests.request("GET", COM_URL_LOGIN)

    d_Login = extraer_datos_session(response_Login)

    s_Login = d_Login[0]  # Session
    c_b_Login = d_Login[1]  # Cookie barracuda
    vs_Login = d_Login[2]  # Viewstate
    payload_Found = 'frmLogin=frmLogin&usuario=' + USUARIO + '&clave=' + CLAVE + \
        '&j_idt18=Ingresar&javax.faces.ViewState=' + \
        urllib.parse.quote(vs_Login, safe="")

    # print(payload_Found)

    headers_Found = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': CABECERA_SESSION + s_Login + '; ' + CABECERA_COOKIE_BARRACUDA + c_b_Login,
        'Origin': COM_URL_BASE_CLOCATOR,
        'Referer': COM_URL_LOGIN,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    response_Found = requests.request(
        "POST", COM_URL_FOUND + s_Login, headers=headers_Found, data=payload_Found)
    # print(respFound.text)

    payload_Main = {}

    headers_Main = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': CABECERA_SESSION + s_Login + '; ' + CABECERA_COOKIE_BARRACUDA + c_b_Login,
        'Referer': COM_URL_LOGIN,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    response_Main = requests.request(
        "GET", COM_URL_MAIN, headers=headers_Main, data=payload_Main)

    #print(response_Main.text)
    return response_Main, s_Login, c_b_Login
