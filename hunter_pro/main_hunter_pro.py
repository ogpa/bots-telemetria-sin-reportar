from hunter_pro.login_hunter_pro import login_hunter_pro
from hunter_pro.ultimo_estado import ultimo_estado
from hunter_pro.productividad import productividad
import pandas as pd
#from hunter.obtener_reporte_productividad import obtener_reporte_productividad
#from hunter.extraer_codigos_placas import extraer_codigos_placas

lista_usuario = [["mbrenting.dpizarro", "mbrenting2022!"],
                 ["dpizarros", "renting22!"]]


def scan_hunter_pro(hora_reporte):

    df_hunter_pro_columnas = ["placa", "descripcion_vehiculo", "fecha", "proveedor", "database", "id", "horas_movimiento",
                          "horas_ralenti", "velocidad_maxima", "dias_uso", "porcentaje_ralenti", "odometro_fin", "odometro_inicio", "distancia"]

    df_hunter_pro = pd.DataFrame(columns=df_hunter_pro_columnas)
    
    for u in lista_usuario:
        l = login_hunter_pro(u)
        df_ue = ultimo_estado(l)
        #print(df_ue)
        df_pr = productividad(l,hora_reporte)
        #print(df_pr)
        df_hunter_pro = pd.concat([df_hunter_pro, df_pr])
    df_hunter_pro.to_csv("hunter_pro_prueba.csv",index=False)
    return df_hunter_pro


#scan_hunter_pro("Hoy")
