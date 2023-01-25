import requests
import urllib
import pandas as pd
import time

FRECUENCIA_CHECK_STATUS_DATASET = 10.0  # Segundos

id_cliente = "45c839e9-c9c1-422a-ab27-f19bc828f1ea"
tenant_name = "mb-renting.com"
id_tenant = "983ebe77-03af-48dc-86a6-9402c8faa106"
id_workspace = "96f6b05f-7e0d-4116-8180-5323e642c737"
id_dataset = "eb3b4b04-334d-4eed-9be1-54e8c0697c23"
id_reporte = "66efa858-bade-4bda-941f-46b313dd322b"
secret = "K3U8Q~KMBTwvtKBhKxGLk52wU5mPLzbx5D-zUaF1"
username = "dpizarro@mb-renting.com"
password = "Renting2023$"
url_token = "https://login.microsoftonline.com/"+id_tenant + "/oauth2/token"

payload_token = 'client_id=' + id_cliente + '&grant_type=password&resource=https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi&client_secret=' + \
    secret + '&username=' + \
    urllib.parse.quote(username, safe="") + '&password=' + \
    urllib.parse.quote(password, safe="")

response_token = requests.request("POST", url_token, data=payload_token)
data = response_token.json()
token = data["access_token"]
# print(data["access_token"])


###################################
# STATUS
###################################

url_status_dataset = "https://api.powerbi.com/v1.0/myorg/groups/" + \
    id_workspace + "/datasets/" + id_dataset + "/refreshes"

headers_status_dataset = {
    "Authorization": "Bearer " + token,
    "Content-type": "application/json"
}


response_status_dataset = requests.request(
    "GET", url_status_dataset, headers=headers_status_dataset)

dict_refresh = response_status_dataset.json()["value"]

df = pd.DataFrame(dict_refresh, columns=[
                  'requestId', 'id', 'refreshType', 'startTime', 'endTime', 'status'])
df.set_index('id')
#df.to_csv("status_power_bi.csv", index=False)
status = df.status[0]

starttime = time.time()
tiempo_status = time.time() - starttime
while (status != "Completed" and tiempo_status < 20.0):
    if tiempo_status < 20.0:
        print("Tiempo menor a 30.0")
    response_status_dataset = requests.request(
        "GET", url_status_dataset, headers=headers_status_dataset)
    dict_refresh = response_status_dataset.json()["value"]

    df = pd.DataFrame(dict_refresh, columns=[
        'requestId', 'id', 'refreshType', 'startTime', 'endTime', 'status'])
    df.set_index('id')
    status = df.status[0]

    time.sleep(FRECUENCIA_CHECK_STATUS_DATASET -
               ((time.time() - starttime) % FRECUENCIA_CHECK_STATUS_DATASET))
    tiempo_status = time.time() - starttime
    print(status)
    print(tiempo_status)
# print(df)

###################################
# ACTUALIZAR
###################################

# url_actualizar_dataset = "https://api.powerbi.com/v1.0/myorg/datasets/" + id_dataset + "/refreshes"

# headers_actualizar_dataset = {
#     "Authorization":"Bearer "+ token,
#     "Content-type": "application/json"
# }
# response_actualizar_dataset = requests.request("POST", url_actualizar_dataset,headers=headers_actualizar_dataset)
# print(response_actualizar_dataset.text)
