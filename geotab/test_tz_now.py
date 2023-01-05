import mygeotab
from datetime import datetime, timedelta

# 2023-01-02T05:00:00.000Z


def ahora():
    hoy = datetime.now() + timedelta(hours=5)  # El 5 es por hora de peru
    hoy_geotab = mygeotab.dates.format_iso_datetime(hoy)
    return hoy_geotab
