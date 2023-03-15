from datetime import timedelta


def extraer_string(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def obtener_fecha_y_hora(d):

    #date = datetime.now()
    d = d - timedelta(hours=5)
    d = str(d)
    # print(d)
    fecha = extraer_string(d, "", " ")
    #f = datetime.datetime.now().date(d)
    hora = extraer_string(d, " ", "+00:00")
    hora = hora[0:5]
    # print(hora)
    # print(hora[:-3])
    return fecha, hora
