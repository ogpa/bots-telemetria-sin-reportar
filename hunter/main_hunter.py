from hunter.login_hunter import login_hunter
from hunter.obtener_reporte_productividad import obtener_reporte_productividad
from hunter.extraer_codigos_placas import extraer_codigos_placas

def scan_hunter(hora_reporte):
    
    l = login_hunter()

    c = extraer_codigos_placas(l)
    print("Códigos de placas extraídos")
    df = obtener_reporte_productividad(c, hora_reporte)
    # subir_s3(p)
    #f = "p.html"
    # with open(f, "w", encoding="utf-8") as f:  # Descomentar para hacer primer request
    #     f.write(p)  # Descomentar para hacer primer request
    # print(p)
    return df

#scan_hunter("Ayer")