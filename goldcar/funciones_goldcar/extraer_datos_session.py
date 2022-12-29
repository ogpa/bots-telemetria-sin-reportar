GOLD_CAB_SIGN = 'o.sign="'
GOLD_FIN_SIGN = '";'
COM_CAB_COOKIE_BARRACUDA = "BNI_BARRACUDA_LB_COOKIE="
COM_FIN_COOKIE_BARRACUDA = "; Path=/; HttpOnly"
COM_CAB_VIEWSTATE = 'id="j_id1:javax.faces.ViewState:0" value="'
COM_FIN_VIEWSTATE = '" autocomplete="off"'
COM_CAB_COOKIE = ""
COM_FIN_COOKIE = '; Domain'
# COM_CAB_VIEWSTATEGENERATOR = 'id="__VIEWSTATEGENERATOR" value="'
# COM_FIN_VIEWSTATEGENERATOR = '"'
# COM_CAB_EVENTVALIDATION = 'id="__EVENTVALIDATION" value="'
# COM_FIN_EVENTVALIDATION = '"'

# cookie,viewstate,viewstategenerator,eventvalidation


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    # empieza a buscar el fin a partir del inicio
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def extraer_datos_session(response):
    sign = extraer_texto(
        response.text, GOLD_CAB_SIGN, GOLD_FIN_SIGN)
    # print(session)

    #cookie_barracuda = extraer_texto(response.headers["Set-Cookie"], COM_CAB_COOKIE_BARRACUDA, COM_FIN_COOKIE_BARRACUDA)
    # print(cookie)

    #viewstate = extraer_texto(response.text, COM_CAB_VIEWSTATE, COM_FIN_VIEWSTATE)
    # print(viewstate)
    #cookie = extraer_texto(response.headers["Set-Cookie"], COM_CAB_COOKIE, COM_FIN_COOKIE)

    return sign
