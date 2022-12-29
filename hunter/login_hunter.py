import requests
import urllib
from funciones_hunter.extraer_datos_session import extraer_datos_session
HUN_URL_BASE = "http://www.huntermonitoreoperu.com"
HUN_URL_LOGIN = "http://www.huntermonitoreoperu.com/GeoV3.3/LoginV3.aspx"
HUN_URL_MAINHTML = "http://www.huntermonitoreoperu.com/GeoV3.3/Paginas/Main.html?r="
HUN_URL_MAIN36 = "http://www.huntermonitoreoperu.com/GeoV3.3/Paginas/Main36.aspx"
HUN_URL_ESTADOFLOTA = "http://www.huntermonitoreoperu.com/GeoV3.3/Paginas/EstadoFlota/Estado.aspx?TIME="
CABECERA_ASPNET = "ASP.NET_SessionId="
USUARIO = "20605414410"
CLAVE = "mb504"


def login_hunter():

    response_Login = requests.request("GET", HUN_URL_LOGIN)

    d_Login = extraer_datos_session(response_Login)

    c_Login = d_Login[0]
    vs_Login = d_Login[1]
    vsg_Login = d_Login[2]
    ev_Login = d_Login[3]

    payload_Loginv3 = '__EVENTTARGET=btningresar&__EVENTARGUMENT=&__VIEWSTATE=' + urllib.parse.quote(vs_Login, safe="") + '&__VIEWSTATEGENERATOR=' + vsg_Login + '&__EVENTVALIDATION=' + urllib.parse.quote(ev_Login, safe="") + '&txusuario=' + USUARIO + '&txclave=' + CLAVE + \
        '&hdintentos=1&vnRegistroWebState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&vnReclamosState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&vnRestablecerState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&bNoticiasState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A39%3A374%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&vnAgenciasState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&DXScript=1_11%2C1_252%2C1_12%2C1_23%2C1_64%2C1_14%2C1_15%2C1_17%2C1_41&DXCss=0_2771%2C1_68%2C1_69%2C0_2776'

    headers_Loginv3 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': CABECERA_ASPNET + c_Login,
        'Origin': HUN_URL_BASE,
        'Referer': HUN_URL_LOGIN,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    response_Loginv3 = requests.request(
        "POST", HUN_URL_LOGIN, headers=headers_Loginv3, data=payload_Loginv3)

    # print(respLoginV3.text)

    headers_Main36 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': CABECERA_ASPNET + c_Login,
        'Origin': HUN_URL_BASE,
        'Referer': HUN_URL_MAINHTML,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    response_Main36 = requests.request(
        "GET", HUN_URL_MAIN36, headers=headers_Main36)

    # print(time_Main36)
    return response_Main36.text
