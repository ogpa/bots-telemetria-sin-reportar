from comsatel import scan_comsatel
from hunter import scan_hunter
from geotab import scan_geotab
import pandas as pd
from datetime import datetime, timezone, timedelta
#UTC -5
ZONA_HORARIA = 5
today = datetime.now(timezone.utc)
today = today - timedelta(hours=ZONA_HORARIA)
hoy = today.strftime("%d-%m-%Y")


#comsatel_df = scan_comsatel(hoy)
geotab_df = scan_geotab(hoy)
hunter_df = scan_hunter(hoy)

#dfs = [hunter_df, geotab_df, comsatel_df]
dfs = [hunter_df, geotab_df]
main_df = pd.concat(dfs)

nombre_archivo = hoy + "_data_telemetria_sin_reportar.csv"
main_df.to_csv(nombre_archivo, index=False)
# s3 = boto3.client('s3')
# with open(nombre_archivo_final_s3, "rb") as f:
#     s3.upload_fileobj(f, S3_BUCKET_NAME,S3_RUTA_FOLDER + nombre_archivo_final)
