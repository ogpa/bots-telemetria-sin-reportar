from comsatel.obtener_reporte_consolidado import obtener_reporte_consolidado
from comsatel.abrir_reportes import abrir_reportes
from comsatel.funciones_comsatel.extraer_datos_session import extraer_datos_session
from comsatel.login_comsatel import login_comsatel
from comsatel.funciones_comsatel.crear_csv import crear_csv


def scan_comsatel(hora_reporte):
    l = login_comsatel()
    d_l = extraer_datos_session(l[0])  # l[0] es la respuesta

    vs_l = d_l[2]  # Viewstate

    # l[1] es la session, l[2] es la cookie barracuda
    a = abrir_reportes(vs_l, l[1], l[2])

    # c es la ruta del archivo local
    c = obtener_reporte_consolidado(a, hora_reporte)
    df = crear_csv(c)
    # subir_s3(c)  # Ruta de archivo
    return df
