import mygeotab
from datetime import datetime, timedelta

# 2023-01-02T05:00:00.000Z


def fechas_ayer_hoy():
    hoy = datetime.now()
    hoy_5 = datetime(hoy.year, hoy.month, hoy.day) + \
        timedelta(hours=5) - timedelta(seconds=1)
    ayer = hoy_5 - timedelta(days=1)+timedelta(seconds=1)
    hoy_geotab = mygeotab.dates.format_iso_datetime(hoy_5)
    # print(hoy_geotab)
    ayer_geotab = mygeotab.dates.format_iso_datetime(ayer)
    # print(ayer_geotab)
    return ayer_geotab, hoy_geotab
