import mygeotab
from datetime import datetime, timedelta
import pandas as pd
from geotab.horas_y_velocidad import horas_y_velocidad
from geotab.distancia import distancia


dbs = ["sanfernando", "bureauveritas",
       "mitsuidelperu", "mibanco", "cofasa", "mb_renting", "agricolachira"]
#dbs = ["sanfernando", "mibanco"]
USUARIO_BOT_GEOTAB = "bot-telemetria@mb-renting.com"
CLAVE_BOT_GEOTAB = "FlotasMBRenting2k23$"


def ayer():
    d = datetime.today() - timedelta(days=1)
    d_p = d.strftime("%Y%m%d")
    d_df = d.strftime("%d/%m/%Y")
    return d_p, d_df


def fecha(delta):
    d = datetime.today() - timedelta(days=delta)
    #fecha_yyyymmdd = d.strftime("%Y%m%d")
    fecha_ddmmyyyy = d.strftime("%d/%m/%Y")
    # return fecha_yyyymmdd, fecha_ddmmyyyy
    return fecha_ddmmyyyy


def scan_geotab(hora_reporte):
    
    df_geotab_columnas = ["placa", "descripcion_vehiculo", "fecha", "proveedor", "database", "id", "horas_movimiento",
                          "horas_ralenti", "velocidad_maxima", "dias_uso", "porcentaje_ralenti", "odometro_fin", "odometro_inicio", "distancia"]

    df_geotab = pd.DataFrame(columns=df_geotab_columnas)

    if hora_reporte == "Ayer":
        fecha_payload = fecha(1)  # dd/mm/yyyy
    elif hora_reporte == "Hoy":
        fecha_payload = fecha(0)  # dd/mm/yyyy

    cant_dbs = len(dbs)

    for x in range(cant_dbs):
        print(dbs[x])
        api = mygeotab.API(username=USUARIO_BOT_GEOTAB,
                           password=CLAVE_BOT_GEOTAB, database=dbs[x])
        credenciales = api.authenticate()
        dsi = api.get('DeviceStatusInfo')

        # print(dsi)
        multi_calls_device = []
        lista_fecha = []
        lista_descripcion_vehiculo = []
        lista_placa = []
        lista_id = []
        lista_proveedor = []
        lista_database = []

        # Obtener aquí la lista de ids y placas
        for s in dsi:
            lista_fecha.append(fecha_payload)
            lista_proveedor.append("Geotab")
            lista_database.append(dbs[x])
            # Obtengo todos los vehículos de esa BD y creo los multicall
            multi_calls_device.append(
                ["Get", dict(typeName="Device", search={"id": s["device"]["id"]})])

        r_multi_device = api.multi_call(multi_calls_device)
        # print(r_multi_device)
        for r in r_multi_device:
            lista_descripcion_vehiculo.append(r[0]["name"])
            lista_placa.append(r[0]["licensePlate"])
            lista_id.append(r[0]["id"])

        dict_datos_vehiculos = {
            "placa": lista_placa,
            "descripcion_vehiculo": lista_descripcion_vehiculo,
            "fecha": lista_fecha,
            "proveedor": lista_proveedor,
            "database": lista_database,
            "id": lista_id
        }
        df_datos_vehiculos = pd.DataFrame(dict_datos_vehiculos)
        df_h_y_v = horas_y_velocidad(lista_id, credenciales, hora_reporte)
        df_distancia = distancia(lista_id, credenciales, hora_reporte)

        df_temp_1 = pd.merge(df_datos_vehiculos, df_h_y_v, on="id", how="left")
        df_temp_1 = df_temp_1.fillna(0)
        df_temp_2 = pd.merge(df_temp_1, df_distancia, on="id")

        df_database = df_temp_2
        # lista_df_database.append(df_database)
        df_geotab = pd.concat([df_geotab, df_database])
        #df_geotab = pd.merge(df_database, df_geotab, on="id", how="left")
        # print(df_database)

        # dict_temp_1 = pd.DataFrame()
        # dict_temp_2 = pd.DataFrame()
        # df_database = pd.DataFrame()
        # df_database = pd.merge(
        #     df_datos_vehiculos, df_h_y_v, on="id", how="left")
        # df_database = df_database.fillna(0)
        # df_database = pd.merge(df_database, df_distancia, on="id")
        # #df_database.to_csv(geotab_csv_filename, index=False)
        # print(df_database)
        # df_geotab = pd.merge(df_database, df_database, on="id")

        #df_geotab.drop_duplicates(subset=["database", "id"])
        #df_geotab = pd.merge(df_geotab, df_database, on="id")
        # lista_df_database.append(df_database)

    # for y in range(cant_dbs):
    #     df_geotab = pd.merge(
    #         lista_df_database[y+1], lista_df_database[y], on="id")

    #df_geotab.to_csv(geotab_csv_filename, index=False)
    return df_geotab


# scan_geotab()
