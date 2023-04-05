from common.seleccionar_hora import seleccionar_hora
from comsatel.main_comsatel import scan_comsatel
from hunter.main_hunter import scan_hunter
from geotab.main_geotab import scan_geotab
from goldcar.main_goldcar import scan_goldcar
from hunter_pro.main_hunter_pro import scan_hunter_pro
import pandas as pd
import boto3
import time

S3_BUCKET_NAME = "apps-mbr-innovacion"
S3_RUTA_FOLDER_PRODUCTIVIDAD = "bi-telemetria/productividad/"


# Ayer u Hoy según la hora actual, Fecha para histórico dd-mm-yyyy
hora_reporte = seleccionar_hora()
print(hora_reporte[0])

# print("Ejecutando Hunter Pro.")
# start_time = time.time()
# hunter_pro_df = scan_hunter_pro(hora_reporte[0])
# #print(hunter_pro_df)
# print("Hunter Pro tardó %s segundos." % (time.time() - start_time))

print("Ejecutando Comsatel.")
start_time = time.time()
comsatel_df = scan_comsatel("Ayer")
print("Comsatel tardó %s segundos." % (time.time() - start_time))

print("Ejecutando Goldcar.")
start_time = time.time()
goldcar_df = scan_goldcar("Ayer")
print("Goldcar tardó %s segundos." % (time.time() - start_time))

print("Ejecutando Geotab.")
start_time = time.time()
geotab_df = scan_geotab("Ayer")
print("Geotab tardó %s segundos." % (time.time() - start_time))

print("Ejecutando Hunter.")
start_time = time.time()
hunter_df = scan_hunter("Ayer")
print("Hunter tardó %s segundos." % (time.time() - start_time))

dfs = [comsatel_df, hunter_df, geotab_df, goldcar_df]
#dfs =[goldcar_df]
#dfs = [comsatel_df, hunter_df, geotab_df, goldcar_df]
main_df = pd.concat(dfs)

nombre_archivo = hora_reporte[0] + "_productividad.csv"
main_df.to_csv(nombre_archivo, index=False)

# s3 = boto3.client('s3')

# if hora_reporte[0] == "Hoy":
#     with open(nombre_archivo, "rb") as f:
#         s3.upload_fileobj(f, S3_BUCKET_NAME,
#                           S3_RUTA_FOLDER_RECIENTE_HOY + nombre_archivo)
# elif hora_reporte[0] == "Ayer":
#     with open(nombre_archivo, "rb") as f:
#         s3.upload_fileobj(f, S3_BUCKET_NAME,
#                           S3_RUTA_FOLDER_HISTORICO + hora_reporte[1] + "_productividad.csv")  # Formato 13-01-2023_productividad.csv
#     with open(nombre_archivo, "rb") as f:
#         s3.upload_fileobj(f, S3_BUCKET_NAME,
#                           S3_RUTA_FOLDER_RECIENTE_AYER + nombre_archivo)

# with open(nombre_archivo, "rb") as f:
#     s3.upload_fileobj(f, S3_BUCKET_NAME,
#                       S3_RUTA_FOLDER_PRODUCTIVIDAD + hora_reporte[1] + "_productividad.csv")  # Formato 13-01-2023_productividad.csv
