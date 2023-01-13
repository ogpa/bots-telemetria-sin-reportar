import mygeotab
from datetime import datetime, timedelta

# 2023-01-02T05:00:00.000Z


def fechas_ayer_hoy(hora_reporte):

    hoy = datetime.now()

    if hora_reporte == "Ayer":

        hoy_5 = datetime(hoy.year, hoy.month, hoy.day) + \
            timedelta(hours=5) - timedelta(seconds=1)
        ayer = hoy_5 - timedelta(days=1)+timedelta(seconds=1)

        fin_geotab = mygeotab.dates.format_iso_datetime(hoy_5)
        inicio_geotab = mygeotab.dates.format_iso_datetime(ayer)
    elif hora_reporte == "Hoy":
        hoy_5 = datetime(hoy.year, hoy.month, hoy.day) + \
            timedelta(hours=5)
        inicio_geotab = mygeotab.dates.format_iso_datetime(hoy_5)
        fin_geotab = mygeotab.dates.format_iso_datetime(
            hoy + timedelta(hours=5))

    return inicio_geotab, fin_geotab
