from funciones_comsatel.subir_s3 import subir_s3
from obtener_reporte_consolidado import obtener_reporte_consolidado
from abrir_reportes import abrir_reportes
from funciones_comsatel.extraer_datos_session import extraer_datos_session
from login_comsatel import login_comsatel
from funciones_comsatel.crear_csv import crear_csv
l = login_comsatel()
d_l = extraer_datos_session(l[0])  # l[0] es la respuesta

vs_l = d_l[2]  # Viewstate

# l[1] es la session, l[2] es la cookie barracuda
a = abrir_reportes(vs_l, l[1], l[2])
c = obtener_reporte_consolidado(a)
crear_csv(c)
# subir_s3(c)  # Ruta de archivo
