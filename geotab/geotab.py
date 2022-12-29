import mygeotab
import pandas as pd
from Funciones.obtener_fecha_y_hora import obtener_fecha_y_hora
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from Funciones.asignar_region import asignar_region
POLY_TALLER_MOLINA = Polygon([(-12.071496, -76.955457), (-12.071008, -76.954843),
                              (-12.070704, -76.953837), (-12.072157, -76.953322), (-12.0726576, -76.954998)])


dbs = ["sanfernando", "bureauveritas", "mitsuiautomotriz", "mibanco"]


def scan_geotab(hoy):

    lista_fecha = []
    lista_hora = []
    lista_deviceid = []
    lista_latitud = []
    lista_longitud = []
    lista_placa = []
    lista_tallermonlina = []
    lista_proveedor = []
    lista_region = []
    cant_dbs = len(dbs)
    for x in range(cant_dbs):

        api = mygeotab.API(username='innovacion@mb-renting.com',
                           password='j4utjs43$$Ah', database=dbs[x])
        api.authenticate()
        dsi = api.get('DeviceStatusInfo')

        multi_calls = []
        multi_calls.clear()

        for s in dsi:
            result_fechahora = obtener_fecha_y_hora(s["dateTime"])
            lista_fecha.append(result_fechahora[0])
            lista_hora.append(result_fechahora[1])
            lista_deviceid.append(s["device"]["id"])
            lista_latitud.append(s["latitude"])
            lista_longitud.append(s["longitude"])
            lista_proveedor.append("Geotab")
            lista_tallermonlina.append(POLY_TALLER_MOLINA.contains(
                Point(s["latitude"], s["longitude"])))
            r = asignar_region(s["latitude"], s["longitude"])
            lista_region.append(r)
            multi_calls.append(
                ["Get", dict(typeName="Device", search={"id": s["device"]["id"]})])

        r_multi = api.multi_call(multi_calls)

        for r in r_multi:
            lista_placa.append(r[0]["name"])

    dict_datos = {
        "Placa": lista_placa,
        "Fecha": lista_fecha,
        "Hora": lista_hora,
        "Latitud": lista_latitud,
        "Longitud": lista_longitud,
        "Deviceid": lista_deviceid,
        "Taller Molina": lista_tallermonlina,
        "Proveedor": lista_proveedor,
        "Region": lista_region
    }

    geotab_df = pd.DataFrame(dict_datos)
    geotab_csv_filename = hoy + "_geotab.csv"
    geotab_df.to_csv(geotab_csv_filename, index=False)
    return geotab_df


# scan_geotab()
