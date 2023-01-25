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

url_access = "https://login.microsoftonline.com/"+id_tenant + "/oauth2/token"
payload_access = "client_id=45c839e9-c9c1-422a-ab27-f19bc828f1ea&grant_type=client_credentials&resource=https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi&client_secret=K3U8Q~KMBTwvtKBhKxGLk52wU5mPLzbx5D-zUaF1"

response_access = requests.request("POST", url_access, data=payload_access)
print(response_access)
print(response_access.text)
