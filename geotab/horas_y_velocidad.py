import mygeotab
from geotab.fechas_ayer_hoy import fechas_ayer_hoy
import pandas as pd


def horas_y_velocidad(lista_id, credenciales, hora_reporte):
    username = credenciales.username
    # print(username)
    database = credenciales.database
    # print(database)
    server = credenciales.server
    # print(server)
    session_id = credenciales.session_id
    # print(session_id)
    multi_calls = []
    multi_calls.clear()
    fechas = fechas_ayer_hoy(hora_reporte)
    inicio = fechas[0]  # "2023-01-03T05:00:00.000Z" ayer
    fin = fechas[1]  # "2023-01-04T04:59:59.000Z" hoy
    # print(ayer)
    # print(hoy)
    for s in lista_id:
        # Obtengo todos los vehículos de esa BD y creo los multicall
        multi_calls.append(
            ["Get", dict(typeName="Trip", search={"fromDate": inicio, "toDate": fin, "deviceSearch": {"id": s}})])

    api = mygeotab.API(username=username, database=database,
                       server=server, session_id=session_id)
    r_trip_multi = api.multi_call(multi_calls)

    # Horas movimiento
    lista_horas_movimiento = []
    lista_horas_ralenti = []
    lista_velocidad_maxima = []
    lista_id_temp = []
    lista_porcentaje_ralenti = []
    lista_dias_uso = []
    # print(lista_id_temp)
    # print(r_trip_multi)
    for trips_placas in r_trip_multi:

        if len(trips_placas) > 0:
            id = trips_placas[0]["device"]["id"]
            # print(id)
            lista_id_temp.append(id)
            suma_movimiento = 0
            suma_ralenti = 0
            actual_maxima = 0
            for t in trips_placas:

                # Movimiento
                temp_movimiento = t["drivingDuration"]
                t_movimiento = (temp_movimiento.hour * 60 + temp_movimiento.minute) * \
                    60 + temp_movimiento.second
                suma_movimiento = suma_movimiento + t_movimiento

                # Ralenti
                temp_ralenti = t["idlingDuration"]
                t_ralenti = (temp_ralenti.hour * 60 + temp_ralenti.minute) * \
                    60 + temp_ralenti.second
                suma_ralenti = suma_ralenti + t_ralenti

                # Velocidad máxima
                v_max_trip = t["maximumSpeed"]
                if v_max_trip > actual_maxima:
                    actual_maxima = v_max_trip

            suma_movimiento = suma_movimiento / 3600
            suma_ralenti = suma_ralenti / 3600

            lista_horas_movimiento.append(suma_movimiento)
            lista_horas_ralenti.append(suma_ralenti)
            lista_velocidad_maxima.append(actual_maxima)

            if suma_ralenti == 0:
                porcentaje_ralenti = 0
            else:
                porcentaje_ralenti = (
                    suma_ralenti/(suma_ralenti + suma_movimiento))

            if suma_movimiento > 0 or suma_ralenti > 0:
                dias_uso = 1
            else:
                dias_uso = 0

            lista_dias_uso.append(dias_uso)
            lista_porcentaje_ralenti.append(porcentaje_ralenti)
    # print(t["idlingDuration"])
    # print(velocidad_maxima, "km/h maxima")
    # print(suma_ralenti/60, "ralenti minutos")

    # print(t["idlingDuration"])
    # print(suma_movimiento/60, "movimiento minutos")
    # Horas ralenti
    # print(r_horas_multi)

    dict_horas_y_velocidad = {
        "id": lista_id_temp,
        "horas_movimiento": lista_horas_movimiento,
        "horas_ralenti": lista_horas_ralenti,
        "velocidad_maxima": lista_velocidad_maxima,
        "dias_uso": lista_dias_uso,
        "porcentaje_ralenti": lista_porcentaje_ralenti
    }
    geotab_df = pd.DataFrame(dict_horas_y_velocidad)
    #geotab_csv_filename = "geotab_horas_y_velocidad.csv"
    #geotab_df.to_csv(geotab_csv_filename, index=False)
    return geotab_df

    # return x
