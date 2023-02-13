HUN_CAB_RETURNURL = ""
HUN_FIN_RETURNURL = ";"
HUN_CAB_ASPXAUTH = '; path=/, '
HUN_FIN_ASPXAUTH = ';'
HUN_CAB_VIEWSTATEGENERATOR = 'id="__VIEWSTATEGENERATOR" value="'
HUN_FIN_VIEWSTATEGENERATOR = '"'
HUN_CAB_EVENTVALIDATION = 'id="__EVENTVALIDATION" value="'
HUN_FIN_EVENTVALIDATION = '"'

# cookie,viewstate,viewstategenerator,eventvalidation


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    # empieza a buscar el fin a partir del inicio
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def extraer_datos_session(response):
    returnurl = extraer_texto(
        response.headers["Set-Cookie"], HUN_CAB_RETURNURL, HUN_FIN_RETURNURL)
    print(returnurl)

    aspxauth = extraer_texto(
        response.headers["Set-Cookie"], HUN_CAB_ASPXAUTH, HUN_FIN_ASPXAUTH)
    print(aspxauth)

    # viewstategenerator = extraer_texto(
    #     response.text, HUN_CAB_VIEWSTATEGENERATOR, HUN_FIN_VIEWSTATEGENERATOR)
    # # print(viewstategenerator_LogIn)

    # eventvalidation = extraer_texto(
    #     response.text, HUN_CAB_EVENTVALIDATION, HUN_FIN_EVENTVALIDATION)
    # # print(eventvalidation_LogIn)
    return returnurl, aspxauth
