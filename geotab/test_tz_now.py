import mygeotab
from datetime import datetime, timedelta

# 2023-01-02T05:00:00.000Z

xd = "2024-01-16T21:15:41.337Z"
def ahora():
    hoy = datetime.now() + timedelta(hours=5)  # El 5 es por hora de peru
    hoy_geotab = mygeotab.dates.format_iso_datetime(hoy)
    print(hoy_geotab)
    if hoy_geotab > xd:
        print (type(hoy_geotab))
        print("La hora actual es mayor.")
    else:
        print (type(hoy_geotab))
        print("La hora actual es menor.")
    #print(hoy_geotab)
    #return hoy_geotab
ahora()