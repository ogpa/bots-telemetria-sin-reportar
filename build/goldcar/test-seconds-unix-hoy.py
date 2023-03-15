from datetime import datetime, timedelta
import pytz


tz_Lima = pytz.timezone('America/Lima')
tiempo_Lima = datetime.now(tz_Lima)

hora_inicio_Lima = datetime(tiempo_Lima.year, tiempo_Lima.month,
                            tiempo_Lima.day)
hora_fin_Lima = datetime(tiempo_Lima.year, tiempo_Lima.month,
                         tiempo_Lima.day) + timedelta(days=1) - timedelta(seconds=1)
hora_inicio_int = str(int(hora_inicio_Lima.timestamp()))
hora_fin_int = str(int(hora_fin_Lima.timestamp()))
#print("Inicio:", hora_inicio_int)
#print("Fin:", hora_fin_int)

# "from":1674104400,"to":1674190799
