import mygeotab
from test_tz_now import ahora
from fechas_ayer_hoy import fechas_ayer_hoy
import pandas as pd

ODOMETRO_METROS_A_KILOMETROS = 1000


def distancia(lista_id, credenciales):
    username = credenciales.username
    # print(username)
    database = credenciales.database
    # print(database)
    server = credenciales.server
    # print(server)
    session_id = credenciales.session_id
    # print(session_id)
    multi_calls_hoy = []
    multi_calls_ayer = []
    multi_calls_hoy.clear()
    multi_calls_ayer.clear()
    fechas = fechas_ayer_hoy()
    ayer = fechas[0]  # "2023-01-03T05:00:00.000Z"
    hoy = fechas[1]  # "2023-01-04T04:59:59.000Z"
    # print(ayer)
    # print(hoy)
    for s in lista_id:
        # Obtengo todos los vehículos de esa BD y creo los multicall
        # print(s)
        multi_calls_hoy.append(
            ["Get", dict(typeName="StatusData", search={"fromDate": hoy, "toDate": hoy, "deviceSearch": {"id": s}, "diagnosticSearch": {"id": "DiagnosticRawOdometerId"}})])
        multi_calls_ayer.append(
            ["Get", dict(typeName="StatusData", search={"fromDate": ayer, "toDate": ayer, "deviceSearch": {"id": s}, "diagnosticSearch": {"id": "DiagnosticRawOdometerId"}})])

    api = mygeotab.API(username=username, database=database,
                       server=server, session_id=session_id)
    r_statusdata_multi_hoy = api.multi_call(multi_calls_hoy)
    r_statusdata_multi_ayer = api.multi_call(multi_calls_ayer)

    lista_odometro_hoy = []
    lista_odometro_ayer = []

    lista_id_temp = []
    # print(r_statusdata_multi_hoy)
    # print(r_statusdata_multi_ayer)
    for status_hoy in r_statusdata_multi_hoy:

        if len(status_hoy) > 0:
            id = status_hoy[0]["device"]["id"]
            lista_id_temp.append(id)
            odometro_hoy = status_hoy[0]["data"]
            lista_odometro_hoy.append(
                odometro_hoy / ODOMETRO_METROS_A_KILOMETROS)

    dict_status_hoy = {
        "id": lista_id_temp,
        "odometro_hoy": lista_odometro_hoy
    }

    df_status_hoy = pd.DataFrame(dict_status_hoy)

    lista_id_temp = []
    lista_id_temp.clear()

    for status_ayer in r_statusdata_multi_ayer:

        if len(status_ayer) > 0:
            id = status_ayer[0]["device"]["id"]
            lista_id_temp.append(id)
            odometro_ayer = status_ayer[0]["data"]
            lista_odometro_ayer.append(
                odometro_ayer / ODOMETRO_METROS_A_KILOMETROS)

    dict_status_ayer = {
        "id": lista_id_temp,
        "odometro_ayer": lista_odometro_ayer
    }

    df_status_ayer = pd.DataFrame(dict_status_ayer)

    df_status = pd.merge(df_status_hoy, df_status_ayer, on="id")
    df_status["distancia"] = df_status.apply(
        lambda x: x["odometro_hoy"]-x["odometro_ayer"], axis=1)

    return df_status
