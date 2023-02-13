from login_hunter_pro import login_hunter_pro
from abrir_reportes import abrir_reportes
#from hunter.obtener_reporte_productividad import obtener_reporte_productividad
#from hunter.extraer_codigos_placas import extraer_codigos_placas


def scan_hunter_pro(hora_reporte):
    
    l = login_hunter_pro()
    rep = abrir_reportes(l)
    # c = extraer_codigos_placas(l)
    # df = obtener_reporte_productividad(c, hora_reporte)
    # subir_s3(p)
    #f = "p.html"
    # with open(f, "w", encoding="utf-8") as f:  # Descomentar para hacer primer request
    #     f.write(p)  # Descomentar para hacer primer request
    # print(p)
    #return df

scan_hunter_pro("Hoy")