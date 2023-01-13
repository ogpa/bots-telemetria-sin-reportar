import mygeotab
from datetime import datetime, timedelta
hoy = datetime.now()
fin_geotab = mygeotab.dates.format_iso_datetime(hoy + timedelta(hours=5))
print(fin_geotab)
