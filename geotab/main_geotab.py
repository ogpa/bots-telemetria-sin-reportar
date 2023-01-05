import mygeotab
from datetime import datetime, timedelta
import pandas as pd
from horas_y_velocidad import horas_y_velocidad
#dbs = ["sanfernando", "bureauveritas","mitsuidelperu", "mibanco", "cofasa", "mb_renting"]
dbs = ["mibanco"]
USUARIO_BOT_GEOTAB = "bot-telemetria@mb-renting.com"
CLAVE_BOT_GEOTAB = "FlotasMBRenting2k23$"


def ayer():
    d = datetime.today() - timedelta(days=1)
    d_p = d.strftime("%Y%m%d")
    d_df = d.strftime("%d/%m/%Y")
    return d_p, d_df


def scan_geotab():

    lista_fecha = []
    lista_descripcion_vehiculo = []
    lista_placa = []
    lista_id = []
    lista_proveedor = []
    fecha_ayer = ayer()
    cant_dbs = len(dbs)
    for x in range(cant_dbs):

        api = mygeotab.API(username=USUARIO_BOT_GEOTAB,
                           password=CLAVE_BOT_GEOTAB, database=dbs[x])
        credenciales = api.authenticate()
        dsi = api.get('DeviceStatusInfo')

        # print(dsi)
        multi_calls_device = []
        multi_calls_device.clear()

        # Obtener aquí la lista de ids y placas
        for s in dsi:
            lista_fecha.append(fecha_ayer[1])
            lista_proveedor.append("Geotab")
            # Obtengo todos los vehículos de esa BD y creo los multicall
            multi_calls_device.append(
                ["Get", dict(typeName="Device", search={"id": s["device"]["id"]})])

        r_multi_device = api.multi_call(multi_calls_device)
        # print(r_multi_device)
        for r in r_multi_device:
            lista_descripcion_vehiculo.append(r[0]["name"])
            lista_placa.append(r[0]["licensePlate"])
            lista_id.append(r[0]["id"])

        h_y_v = horas_y_velocidad(lista_id, credenciales)

    # dict_datos = {
    #     "placa": lista_placa,
    #     "fecha": lista_fecha,
    #     "proveedor": lista_proveedor,
    # }

    # geotab_df = pd.DataFrame(dict_datos)
    # geotab_csv_filename = hoy + "_geotab.csv"
    # geotab_df.to_csv(geotab_csv_filename, index=False)
    # return geotab_df
scan_geotab()
