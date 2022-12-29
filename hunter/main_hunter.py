from login_hunter import login_hunter
from obtener_reporte_productividad import obtener_reporte_productividad
from extraer_codigos_placas import extraer_codigos_placas
from funciones_hunter.subir_s3 import subir_s3
l = login_hunter()
c = extraer_codigos_placas(l)
p = obtener_reporte_productividad(c)
subir_s3(p)
#f = "p.html"
# with open(f, "w", encoding="utf-8") as f:  # Descomentar para hacer primer request
#     f.write(p)  # Descomentar para hacer primer request
# print(p)
