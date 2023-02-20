from login_hunter_pro import login_hunter_pro
from ultimo_estado import ultimo_estado
from productividad import productividad
#from hunter.obtener_reporte_productividad import obtener_reporte_productividad
#from hunter.extraer_codigos_placas import extraer_codigos_placas

lista_usuario = [["mbrenting.dpizarro", "mbrenting2022!"],
                 ["dpizarros", "renting22!"]]


def scan_hunter_pro(hora_reporte):

    for u in lista_usuario:
        l = login_hunter_pro(u)
        df_ue = ultimo_estado(l)
        print(df_ue)
        df_pr = productividad(l)
        print(df_pr)
    return df_pr


scan_hunter_pro("Hoy")
