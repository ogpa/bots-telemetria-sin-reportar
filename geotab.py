import mygeotab
import pandas as pd
from obtener_fecha_y_hora import obtener_fecha_y_hora

api = mygeotab.API(username='innovacion@mb-renting.com',
                   password='j4utjs43$$Ah', database='sanfernando')
api.authenticate()


dsi = api.get('DeviceStatusInfo')

multi_calls = []

lista_fecha = []
lista_hora = []
lista_deviceid = []
lista_latitud = []
lista_longitud = []
lista_placa = []


for s in dsi:
    result_fechahora = obtener_fecha_y_hora(s["dateTime"])
    lista_fecha.append(result_fechahora[0])
    lista_hora.append(result_fechahora[1])
    lista_deviceid.append(s["device"]["id"])
    lista_latitud.append(s["latitude"])
    lista_longitud.append(s["longitude"])
    multi_calls.append(
        ["Get", dict(typeName="Device", search={"id": s["device"]["id"]})])

r_multi = api.multi_call(multi_calls)

for r in r_multi:
    lista_placa.append(r[0]["name"])

dict_datos = {
    "placa": lista_placa,
    "fecha": lista_fecha,
    "hora": lista_hora,
    "latitud": lista_latitud,
    "longitud": lista_longitud,
    "deviceid": lista_deviceid
}
geotab_df = pd.DataFrame(dict_datos)
csv_filename = "geotab.csv"
geotab_df.to_csv(csv_filename, index=False)
