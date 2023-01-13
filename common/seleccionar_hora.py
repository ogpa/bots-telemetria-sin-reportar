from datetime import datetime
import pytz


def seleccionar_hora():

    tz_Lima = pytz.timezone('America/Lima')
    tiempo_Lima = datetime.now(tz_Lima)
    hora_Lima = tiempo_Lima.hour
    #print("Lima:", datetime_NY.strftime("%H:%M:%S"))
    print("Horas Lima:", hora_Lima)
    if hora_Lima <= 9:
        #print("Reporte ayer")
        hora_reporte = "Ayer"
    # elif hora_Lima <= 12:
    #     #print("Reporte ayer")
    #     hora_reporte = "Hoy Mañana"
    # elif hora_Lima <= 17:
    #     #print("Reporte ayer")
    #     hora_reporte = "Hoy Tarde"
    else:
        hora_reporte = "Hoy"
        #print("No se ejecutará nigún reporte hasta mañana.")

    return hora_reporte
