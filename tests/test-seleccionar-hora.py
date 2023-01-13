from datetime import datetime
import pytz

tz_Lima = pytz.timezone('America/Lima')
tiempo_Lima = datetime.now(tz_Lima)
hora_Lima = tiempo_Lima.hour
print("Lima:", tiempo_Lima.strftime("%d/%m/%Y"))
# print("Horas Lima:", hora_Lima)
# if hora_Lima <= 8:
#     print("Reporte ayer")
# elif hora_Lima <= 12:
#     print("Reporte mañana")
# elif hora_Lima <= 17:
#     print("Reporte tarde")
# else:
#     print("Son más de las 5pm.")
