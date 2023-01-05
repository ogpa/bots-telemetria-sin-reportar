import mygeotab
from datetime import datetime, timedelta
from test_tz_now import ahora
import pandas as pd
from mygeotab import API
USUARIO_BOT_GEOTAB = "bot-telemetria@mb-renting.com"
CLAVE_BOT_GEOTAB = "FlotasMBRenting2k23$"


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    # empieza a buscar el fin a partir del inicio
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def convertir_hhmmss(hhmmss):
    if hhmmss == " :00" or hhmmss == "0":
        hora = 0
    else:
        # Obtener los 3 datos de hh:mm:ss
        h = extraer_texto(hhmmss, "", ":")
        # print(h)
        h = int(h)
        m = extraer_texto(hhmmss, ":", ":")
        # print(m)
        m = int(m)
        s = hhmmss[-2:]
        # print(s)
        s = int(s)
        hora = h + m/60 + s/3600
    return hora


api = mygeotab.API(username=USUARIO_BOT_GEOTAB,
                   password=CLAVE_BOT_GEOTAB, database="mb_renting", server="my.geotab.com")
credenciales = api.authenticate()
#dsi = api.get('DeviceStatusInfo')

# device = api.multi_call(
#     [["Get", dict(typeName="Device", search={"id": "b50"})]])
# print(device[0][0]["licensePlate"])

# statusdata = api.multi_call(
#    [["Get", dict(typeName="StatusData", deviceSearch={"id": "b50"})]])

# Aquí está imprimiendo todos los DiagnosticRawOdometerId del día anterior
# statusdata = api.get("StatusData", search={"fromDate": "2023-01-02T05:00:00.000Z", "toDate": "2023-01-03T05:00:00.000Z", "deviceSearch": {"id": "b50"},
#                                           "diagnosticSearch": {"id": "DiagnosticRawOdometerId"}})
# statusdata = api.call(method="Get", typeName="StatusData", search={"fromDate": "2023-01-02T05:00:00.000Z", "toDate": "2023-01-03T05:00:00.000Z", "deviceSearch": {"id": "b50"},
#                                                                    "diagnosticSearch": {"id": "DiagnosticRawOdometerId"}})

# trip = api.call(method="Get", typeName="Trip", search={
#    "fromDate": "2023-01-03T05:00:00.000Z", "toDate": "2023-01-04T04:59:59.000Z", "deviceSearch": {"id": "b50"}})

# print(trip)
#suma_ralenti = 0
# for t in trip:

#     #t_ralenti = convertir_hhmmss(t["idlingDuration"])
#     temp_ralenti = t["idlingDuration"]
#     t_ralenti = (temp_ralenti.hour * 60 + temp_ralenti.minute) * \
#         60 + temp_ralenti.second
#     suma_ralenti = suma_ralenti + t_ralenti
#     # print(t["idlingDuration"])
# print(suma_ralenti/60, "ralenti minutos")

# suma_movimiento = 0
# for t in trip:

#     #t_ralenti = convertir_hhmmss(t["idlingDuration"])
#     temp_movimiento = t["drivingDuration"]
#     t_movimiento = (temp_movimiento.hour * 60 + temp_movimiento.minute) * \
#         60 + temp_movimiento.second
#     suma_movimiento = suma_movimiento + t_movimiento
#     # print(t["idlingDuration"])
# print(suma_movimiento/60, "movimiento minutos")

# Odómetro REAL
#hora = ahora()
# odometro_actual = api.call(method="Get", typeName="StatusData", search={"fromDate": hora, "toDate": hora, "deviceSearch": {"id": "b50"},
#                                                                 "diagnosticSearch": {"id": "DiagnosticRawOdometerId"}})
# print(odometro_actual)

# Diferencia de odómetros (distancia) de ayer

# Odómetro REAL
hora = ahora()
# odometro_inicio_ayer = api.call(method="Get", typeName="StatusData", search={"fromDate": "2023-01-03T05:00:00.000Z", "toDate": "2023-01-03T05:00:00.000Z", "deviceSearch": {"id": "b50"},
#                                                                              "diagnosticSearch": {"id": "DiagnosticRawOdometerId"}})
# odometro_fin_ayer = api.call(method="Get", typeName="StatusData", search={"fromDate": "2023-01-04T05:00:00.000Z", "toDate": "2023-01-04T05:00:00.000Z", "deviceSearch": {"id": "b50"},
#                                                                           "diagnosticSearch": {"id": "DiagnosticRawOdometerId"}})
# print(odometro_inicio_ayer[0]["data"])
# print(odometro_fin_ayer[0]["data"])

# km_ayer = odometro_fin_ayer[0]["data"] - odometro_inicio_ayer[0]["data"]
# print(km_ayer/1000, "kms")


# Odómetro GPS
# id: b70
print(hora)
# odometro_gps_actual = api.call(method="Get", typeName="StatusData", search={
#     "deviceSearch": {"id": "b70"}, "diagnosticSearch": {"id": "DiagnosticOdometerAdjustmentId"}})
# print(odometro_gps_actual)

# odometro_gps_inicio_ayer = api.call(method="Get", typeName="StatusData", search={"fromDate": "2023-01-03T05:00:00.000Z", "toDate": "2023-01-03T05:00:00.000Z", "deviceSearch": {"id": "b70"},
#                                                                                  "diagnosticSearch": {"id": "DiagnosticOdometerAdjustmentId"}})
# odometro_gps_fin_ayer = api.call(method="Get", typeName="StatusData", search={"fromDate": "2023-01-04T05:00:00.000Z", "toDate": "2023-01-04T05:00:00.000Z", "deviceSearch": {"id": "b70"},
#                                                                               "diagnosticSearch": {"id": "DiagnosticOdometerAdjustmentId"}})
# print(odometro_gps_inicio_ayer[0]["data"])
# print(odometro_gps_fin_ayer[0]["data"])

# km_ayer = odometro_gps_fin_ayer[0]["data"] - \
#     odometro_gps_inicio_ayer[0]["data"]
# print(km_ayer/1000, "kms")


# Velocidad máxima ayer
# trip = api.call(method="Get", typeName="Trip", search={
#     "fromDate": "2023-01-03T05:00:00.000Z", "toDate": "2023-01-04T04:59:59.000Z", "deviceSearch": {"id": "b50"}})
# velocidad_maxima = 0
# for t in trip:

#     #t_ralenti = convertir_hhmmss(t["idlingDuration"])
#     v_max_trip = t["maximumSpeed"]
#     if v_max_trip > velocidad_maxima:
#         velocidad_maxima = v_max_trip
#     # print(t["idlingDuration"])
# print(velocidad_maxima, "km/h maxima")

# Falta:
# % ralenti
# dias de uso
# proveedor
# fecha
print(credenciales.session_id)
