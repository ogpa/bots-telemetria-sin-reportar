from bs4 import BeautifulSoup


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    # empieza a buscar el fin a partir del inicio
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def extraer_codigos_placas(login):
    temp = []
    lista_codigos_placas = []
    doc = BeautifulSoup(login, "html.parser")
    for s in doc.find_all(
            "select", {"name": "vnGestionConductor$cbConductoresPlaca"}):
        for o in s.find_all("option"):
            temp.append(o)
    # print(temp)

    for p in temp:
        #c = extraer_texto(p, 'value="', '"')
        lista_codigos_placas.append(p["value"])
    # print(lista_codigos_placas)
    lista_codigos_placas = lista_codigos_placas[2:]
    #lista_codigos_placas = lista_codigos_placas[:-1]
    return lista_codigos_placas
