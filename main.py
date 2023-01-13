from common.seleccionar_hora import seleccionar_hora
from comsatel.main_comsatel import scan_comsatel
from hunter.main_hunter import scan_hunter
from geotab.main_geotab import scan_geotab
from selenium_goldcar.main_goldcar import scan_goldcar
import pandas as pd
import boto3
from datetime import datetime, timezone, timedelta

S3_BUCKET_NAME = "apps-mbr"
S3_RUTA_FOLDER_HISTORICO = "bi-telemetria/productividad/historico/"
S3_RUTA_FOLDER_RECIENTE_HOY = "bi-telemetria/productividad/reciente/hoy/"
S3_RUTA_FOLDER_RECIENTE_AYER = "bi-telemetria/productividad/reciente/ayer/"


hora_reporte = seleccionar_hora()  # Ayer u Hoy según la hora actual
print(hora_reporte)

print("Ejecutando Comsatel.")
comsatel_df = scan_comsatel("Ayer")
print("Ejecutando Hunter.")
hunter_df = scan_hunter(hora_reporte)
print("Ejecutando Geotab.")
geotab_df = scan_geotab(hora_reporte)
print("Ejecutando Goldcar.")
goldcar_df = scan_goldcar(hora_reporte)

dfs = [comsatel_df, hunter_df, geotab_df, goldcar_df]

main_df = pd.concat(dfs)

nombre_archivo = hora_reporte + "_productividad.csv"
main_df.to_csv(nombre_archivo, index=False)

s3 = boto3.client('s3')

if hora_reporte == "Hoy":
    with open(nombre_archivo, "rb") as f:
        s3.upload_fileobj(f, S3_BUCKET_NAME,
                          S3_RUTA_FOLDER_RECIENTE_HOY + nombre_archivo)
elif hora_reporte == "Ayer":
    with open(nombre_archivo, "rb") as f:
        s3.upload_fileobj(f, S3_BUCKET_NAME,
                          S3_RUTA_FOLDER_HISTORICO + nombre_archivo)
    with open(nombre_archivo, "rb") as f:
        s3.upload_fileobj(f, S3_BUCKET_NAME,
                          S3_RUTA_FOLDER_RECIENTE_AYER + nombre_archivo)
