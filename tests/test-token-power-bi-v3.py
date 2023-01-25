import requests
import msal
import json
import pandas as pd

id_cliente = "45c839e9-c9c1-422a-ab27-f19bc828f1ea"
tenant_name = "mb-renting.com"
id_tenant = "983ebe77-03af-48dc-86a6-9402c8faa106"
id_workspace = "96f6b05f-7e0d-4116-8180-5323e642c737"
id_dataset = "eb3b4b04-334d-4eed-9be1-54e8c0697c23"
id_reporte = "66efa858-bade-4bda-941f-46b313dd322b"
secret = "K3U8Q~KMBTwvtKBhKxGLk52wU5mPLzbx5D-zUaF1"
username = "dpizarro@mb-renting.com"
password = "Renting2023$"

authority_url = "https://login.microsoftonline.com/" + tenant_name
scope = ["https://analysis.windows.net/powerbi/api/.default"]
url = "https://api.powerbi.com/v1.0/myorg/groups/" + \
    id_workspace + "/datasets/" + id_dataset + "/refreshes?$top=1"


# Use MSAL to grab token

app = msal.ConfidentialClientApplication(
    id_cliente, authority=authority_url, client_credential=secret)
result = app.acquire_token_for_client(scopes=scope)
print(result)
# Get latest Power BI Dataset Refresh

access_token = result['access_token']
header = {'Content-Type': 'application/json',
          'Authorization': f'Bearer {access_token}'}
api_call = requests.get(url=url, headers=header)

# result = api_call.json()['value']

# df = pd.DataFrame(result, columns=[
#     'requestId', 'id', 'refreshType', 'startTime', 'endTime', 'status'])
# df.set_index('id')


# if df.status[0] == "Unknown":
#     print("Dataset is refreshing right now. Please wait until this refresh has finished to trigger a new one.")
# elif df.status[0] == "Disabled":
#     print("Dataset refresh is disabled. Please enable it.")
# elif df.status[0] == "Failed":
#     print("Last Dataset refresh failed. Please check error message.")
# elif df.status[0] == "Completed":
#     api_call = requests.post(url=url, headers=header)
#     print("We triggered a Dataset refresh.")
# else:
#     print("Not familiar with status, please check documentatino for status: '" +
#           df.status[0] + "'")
