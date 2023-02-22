import requests
import urllib
from hunter_pro.funciones_hunter_pro.extraer_datos_session import extraer_datos_session

HUN_URL_BASE = "http://www.huntermonitoreopro.com"
HUN_URL_LOGIN = "https://huntermonitoreopro.com/Account/LogOn?"
HUN_URL_LOGINV3 = "https://huntermonitoreopro.com/Account/LogOnV3/?DistyLanguageOptionId=82"
HUN_URL_CONFIG = "https://huntermonitoreopro.com/Config?returnurl="
HUN_URL_LIVE = "https://huntermonitoreopro.com/live/"
HUN_URL_ESTADOFLOTA = "http://www.huntermonitoreoperu.com/GeoV3.3/Paginas/EstadoFlota/Estado.aspx?TIME="
CABECERA_ASPNET = "ASP.NET_SessionId="
FIN_ASPNET = ";"


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def login_hunter_pro(usuario):

    response_Login = requests.request("GET", HUN_URL_LOGIN)

    #payload_Loginv3 = "LanguageOptionId=82&username=" + usuario + "&password=" + clave + "&action=log+on&"
    payload_Loginv3 = "LanguageOptionId=82&username=" + \
        usuario[0] + "&password=" + usuario[1]+"&action=log+on&"
    headers_Loginv3 = {
        'authority': 'huntermonitoreopro.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': HUN_URL_BASE,
        'referer': HUN_URL_LOGIN,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    response_Loginv3 = requests.request(
        "POST", HUN_URL_LOGINV3, headers=headers_Loginv3, data=payload_Loginv3)

    # print(response_Loginv3.headers["Set-Cookie"])

    d_Loginv3 = extraer_datos_session(response_Loginv3)

    rurl_Login = d_Loginv3[0]
    aspx_Login = d_Loginv3[1]

    payload_Config = {}
    headers_Config = {
        'authority': 'huntermonitoreopro.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en',
        'cookie': rurl_Login + "; " + aspx_Login,
        'referer': HUN_URL_LOGIN,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Config = requests.request(
        "GET", HUN_URL_CONFIG, headers=headers_Config, data=payload_Config)

    payload_Live = {}
    headers_Live = {
        'authority': 'huntermonitoreopro.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en',
        'cookie': rurl_Login + "; " + aspx_Login,
        'referer': HUN_URL_LOGIN,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Live = requests.request(
        "GET", HUN_URL_LIVE, headers=headers_Live, data=payload_Live)

    # print(response_Live.text)

    cookie_asp = extraer_texto(
        response_Live.headers["Set-Cookie"], CABECERA_ASPNET, FIN_ASPNET)
    # vsg_Login = d_Login[2]
    # ev_Login = d_Login[3]

    # payload_Loginv3 = '__EVENTTARGET=btningresar&__EVENTARGUMENT=&__VIEWSTATE=' + urllib.parse.quote(vs_Login, safe="") + '&__VIEWSTATEGENERATOR=' + vsg_Login + '&__EVENTVALIDATION=' + urllib.parse.quote(ev_Login, safe="") + '&txusuario=' + USUARIO + '&txclave=' + CLAVE + \
    #     '&hdintentos=1&vnRegistroWebState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&vnReclamosState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&vnRestablecerState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&bNoticiasState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A39%3A374%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&vnAgenciasState=%7B%26quot%3BwindowsState%26quot%3B%3A%26quot%3B0%3A0%3A-1%3A0%3A0%3A0%3A-10000%3A-10000%3A1%3A0%3A0%3A0%26quot%3B%7D&DXScript=1_11%2C1_252%2C1_12%2C1_23%2C1_64%2C1_14%2C1_15%2C1_17%2C1_41&DXCss=0_2771%2C1_68%2C1_69%2C0_2776'

    # headers_Loginv3 = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
    #     'Cache-Control': 'max-age=0',
    #     'Connection': 'keep-alive',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Cookie': CABECERA_ASPNET + c_Login,
    #     'Origin': HUN_URL_BASE,
    #     'Referer': HUN_URL_LOGIN,
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    # }

    # response_Loginv3 = requests.request(
    #     "POST", HUN_URL_LOGIN, headers=headers_Loginv3, data=payload_Loginv3)

    # # print(respLoginV3.text)

    # headers_Main36 = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'Accept-Language': 'en,en-US;q=0.9,es;q=0.8,it;q=0.7',
    #     'Cache-Control': 'max-age=0',
    #     'Connection': 'keep-alive',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Cookie': CABECERA_ASPNET + c_Login,
    #     'Origin': HUN_URL_BASE,
    #     'Referer': HUN_URL_MAINHTML,
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    # }

    # response_Main36 = requests.request(
    #     "GET", HUN_URL_MAIN36, headers=headers_Main36)

    # # print(time_Main36)
    return cookie_asp, rurl_Login, aspx_Login

# login_hunter_pro()
