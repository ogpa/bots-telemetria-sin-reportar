import requests
import urllib
from funciones_goldcar.extraer_datos_session import extraer_datos_session
from funciones_goldcar.obtener_millis import obtener_millis
from funciones_goldcar.obtener_millis_now import obtener_millis_now
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run_flow
from oauth2client.file import Storage
import json
import os
import re
import httplib2
from oauth2client import GOOGLE_REVOKE_URI, GOOGLE_TOKEN_URI, client
import requests
import pandas as pd
GOLD_URL_LOGIN = "http://gpsenperu.gpsgoldcar.com/"
GOLD_URL_OAUTH = "http://gpsenperu.gpsgoldcar.com/oauth.html"
GOLD_URL_MONITORING_LOGIN = "http://gpsenperu.gpsgoldcar.com/frontend/monitoring_login_bac3329bea18834ef562.js"
GOLD_URL_TAG_MANAGER = "http://www.googletagmanager.com/gtm.js?id=GTM-PMGGDP"
GOLD_URL_G_L6 = "http://www.googletagmanager.com/gtag/js?id=G-L6NP7TDMF6&l=dataLayer&cx=c"
GOLD_URL_GA = "http://www.google-analytics.com/ga.js"
USUARIO = "mbrenting"
CLAVE = "mbrenting2021"


def login_goldcar():
    response_Login = requests.request("GET", GOLD_URL_LOGIN)
    d_Login = extraer_datos_session(response_Login)
    session = requests.Session()
    session.get(GOLD_URL_LOGIN)
    session.get(GOLD_URL_GA)
    headers_GA = {
        'authority': 'www.google-analytics.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'referer': GOLD_URL_LOGIN,
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    session.get(GOLD_URL_GA, headers=headers_GA)
    print(session.cookies)
    # https://stackoverflow.com/questions/29928591/not-getting-all-cookie-info-using-python-requests-module
    # session.get("http://gpsgoldcar.com")
    # session.get("https://gpsgoldcar.com")
    # session.get("http://gpsenperu.gpsgoldcar.com")
    # session.get("http://gpsenperu.gpsgoldcar.com/")
    # print(session.cookies)
    # print(session.headers)
    # print(d_Login)
    # session = requests.Session()
    # r = requests.post("http://google.com")
    # a = r.cookies.get_dict()
    # print(response_Login.headers)
    ga_inicio = obtener_millis(response_Login.headers["Date"])
    # https://stackoverflow.com/questions/25091976/python-requests-get-cookies
    print(ga_inicio)
    payload_Monitoring_Login = {}
    # Usar selenium y requests a la vez
    headers_Monitoring_Login = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': GOLD_URL_LOGIN,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response_Monitoring_Login = requests.request(
        "GET", GOLD_URL_MONITORING_LOGIN, headers=headers_Monitoring_Login, data=payload_Monitoring_Login)
    # print(response_Monitoring_Login.cookies)
    # print(response_Monitoring_Login.text)

    payload_Tag_Manager = {}
    headers_Tag_Manager = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': GOLD_URL_LOGIN,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response_Tag_Manager = requests.request(
        "GET", GOLD_URL_TAG_MANAGER, headers=headers_Tag_Manager, data=payload_Tag_Manager)
    # print(response_Tag_Manager.headers)
    # print(response_Tag_Manager.text)

    payload_GL6 = {}
    headers_GL6 = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response_GL6 = requests.request(
        "GET", GOLD_URL_G_L6, headers=headers_GL6, data=payload_GL6)
    # print(response_GL6.headers)
    # print(response_GL6.text)

    payload_Oauth = 'wialon_sdk_url=https%3A%2F%2Fhst-api.wialon.com&client_id=GPS%2BGOLDCAR&access_type=-1&activation_time=0&duration=2592000&flags=7&response_type=hash&sign=' + \
        urllib.parse.quote(d_Login, safe="") + '&login=' + USUARIO + '&passw=' + CLAVE + \
        '&redirect_uri=http%3A%2F%2Fgpsenperu.gpsgoldcar.com%2Fpost_message.html&request_id=1'
    # print(payload_Oauth)
    ga_fin = obtener_millis_now()
    headers_Oauth = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': "gpsenperu.gpsgoldcar.com",
        'Cookie': "lang=en; _ga_L6NP7TDMF6=GS1.1." + ga_inicio + ".1.0." + ga_fin + ".0.0.0",
        'Origin': "http://gpsenperu.gpsgoldcar.com",
        'Referer': GOLD_URL_LOGIN,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    response_Oauth = requests.request(
        "POST", GOLD_URL_OAUTH, headers=headers_Oauth, data=payload_Oauth)
    print(response_Oauth.headers)
# return x
# login_goldcar()
