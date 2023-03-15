import mygeotab
from geotab.fechas_ayer_hoy import fechas_ayer_hoy
import pandas as pd

ODOMETRO_METROS_A_KILOMETROS = 1000


def distancia(lista_id, credenciales, hora_reporte):
    username = credenciales.username
    # print(username)
    database = credenciales.database
    # print(database)
    server = credenciales.server
    # print(server)
    session_id = credenciales.session_id
    # print(session_id)
    multi_calls_fin = []
    multi_calls_inicio = []
    multi_calls_fin.clear()
    multi_calls_inicio.clear()
    fechas = fechas_ayer_hoy(hora_reporte)
    inicio = fechas[0]  # "2023-01-03T05:00:00.000Z"
    fin = fechas[1]  # "2023-01-04T04:59:59.000Z"
    # print(ayer)
    # print(hoy)
    for s in lista_id:
        # Obtengo todos los vehículos de esa BD y creo los multicall
        # print(s)
        multi_calls_fin.append(
            ["Get", dict(typeName="StatusData", search={"fromDate": fin, "toDate": fin, "deviceSearch": {"id": s}, "diagnosticSearch": {"id": "DiagnosticRawOdometerId"}})])
        multi_calls_inicio.append(
            ["Get", dict(typeName="StatusData", search={"fromDate": inicio, "toDate": inicio, "deviceSearch": {"id": s}, "diagnosticSearch": {"id": "DiagnosticRawOdometerId"}})])

    api = mygeotab.API(username=username, database=database,
                       server=server, session_id=session_id)
    r_statusdata_multi_fin = api.multi_call(multi_calls_fin)
    r_statusdata_multi_inicio = api.multi_call(multi_calls_inicio)

    lista_odometro_fin = []
    lista_odometro_inicio = []

    lista_id_temp = []
    # print(r_statusdata_multi_fin)
    # print(r_statusdata_multi_inicio)
    for status_fin in r_statusdata_multi_fin:

        if len(status_fin) > 0:
            id = status_fin[0]["device"]["id"]
            lista_id_temp.append(id)
            odometro_fin = status_fin[0]["data"]
            lista_odometro_fin.append(
                odometro_fin / ODOMETRO_METROS_A_KILOMETROS)

    dict_status_fin = {
        "id": lista_id_temp,
        "odometro_fin": lista_odometro_fin
    }

    df_status_fin = pd.DataFrame(dict_status_fin)

    lista_id_temp = []
    lista_id_temp.clear()

    for status_inicio in r_statusdata_multi_inicio:

        if len(status_inicio) > 0:
            id = status_inicio[0]["device"]["id"]
            lista_id_temp.append(id)
            odometro_inicio = status_inicio[0]["data"]
            lista_odometro_inicio.append(
                odometro_inicio / ODOMETRO_METROS_A_KILOMETROS)

    dict_status_inicio = {
        "id": lista_id_temp,
        "odometro_inicio": lista_odometro_inicio
    }

    df_status_inicio = pd.DataFrame(dict_status_inicio)

    df_status = pd.merge(df_status_fin, df_status_inicio, on="id")
    df_status["distancia"] = df_status.apply(
        lambda x: x["odometro_fin"]-x["odometro_inicio"], axis=1)

    return df_status
