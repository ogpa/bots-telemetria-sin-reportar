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


def lambda_handler(event, context):

    # app_id = id_cliente
    # tenant_id = tenant_name

    # authority_url = 'https://login.microsoftonline.com/' + tenant_id
    # scopes = ['https://analysis.windows.net/powerbi/api/.default']

    # # Step 1. Generate Power BI Access Token
    # #client = msal.ConfidentialClientApplication(id_cliente, authority=authority_url, client_credential=secret)
    # #token_response = client.acquire_token_by_username_password(username=username, password=password, scopes=scopes)
    # #print(token_response)
    # #if not 'access_token' in token_response:
    # #   raise Exception(token_response['error_description'])

    # #access_id = token_response.get('access_token')
    # #return access_id

    # #access_id = request_access_token()

    # #dataset_id = ''
    # endpoint = "https://api.powerbi.com/v1.0/myorg/datasets/eb3b4b04-334d-4eed-9be1-54e8c0697c23/refreshes"
    # headers = {
    #     'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTgzZWJlNzctMDNhZi00OGRjLTg2YTYtOTQwMmM4ZmFhMTA2LyIsImlhdCI6MTY3NDUxNTU0MywibmJmIjoxNjc0NTE1NTQzLCJleHAiOjE2NzQ1MjEwMTQsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBVFFBeS84VEFBQUF3NXc5OFhYMTdoYXJRTVh6VnZSZlovRnpnZnhqS1JSSis5Szh3SGcxMzV4SG5WV0NPblAyZDVMTlhuekpLdUNlIiwiYW1yIjpbInB3ZCJdLCJhcHBpZCI6IjQ1YzgzOWU5LWM5YzEtNDIyYS1hYjI3LWYxOWJjODI4ZjFlYSIsImFwcGlkYWNyIjoiMSIsImZhbWlseV9uYW1lIjoiUGl6YXJybyBTYWx2YWRvciIsImdpdmVuX25hbWUiOiJEaWVnbyBQYXVsIiwiaXBhZGRyIjoiMTkwLjIxNi4xMjQuODIiLCJuYW1lIjoiRGllZ28gUGF1bCBQaXphcnJvIFNhbHZhZG9yIiwib2lkIjoiZjkzMzFhYjAtNDJkNS00NDEwLTg1MmYtZWZhN2EzOGQxMjczIiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTI3MjgwOTM4Ny0yNzMzNTIyNTE1LTgyODM5NzAxNC0xNTMwIiwicHVpZCI6IjEwMDMyMDAxMkZGNjM0RjciLCJyaCI6IjAuQVVZQWQ3NC1tSzhEM0VpR3BwUUN5UHFoQmdrQUFBQUFBQUFBd0FBQUFBQUFBQUJHQUZFLiIsInNjcCI6IkRhc2hib2FyZC5SZWFkLkFsbCBEYXNoYm9hcmQuUmVhZFdyaXRlLkFsbCBEYXRhc2V0LlJlYWQuQWxsIERhdGFzZXQuUmVhZFdyaXRlLkFsbCBSZXBvcnQuUmVhZC5BbGwgUmVwb3J0LlJlYWRXcml0ZS5BbGwgV29ya3NwYWNlLlJlYWQuQWxsIFdvcmtzcGFjZS5SZWFkV3JpdGUuQWxsIiwic3ViIjoiYjVXbmdEcGl3eXBQRlVMc1JDN0I2TXhsQ2UtODRuaUdZNzVvQURndDhKOCIsInRpZCI6Ijk4M2ViZTc3LTAzYWYtNDhkYy04NmE2LTk0MDJjOGZhYTEwNiIsInVuaXF1ZV9uYW1lIjoiZHBpemFycm9AbWItcmVudGluZy5jb20iLCJ1cG4iOiJkcGl6YXJyb0BtYi1yZW50aW5nLmNvbSIsInV0aSI6Ik5WSEUxVlVlUEVLSWFDbUJoZjg3QUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdfQ.WbyP0t-g_4zDeKtIlDKfjhHb6ARwCdGxoOhlsvnbBrDndrZbV_VVRrC_Smg_KcB56Rk2RzLuDl9vyDtaMNcRbh-NQzSTzMy6ZyDG5X4w324T1rqwuEpRCdwddFwGQabWKL3egITOrgFFiFfkkSXPHhH6iWk_hL2KoZAuruhRj1umBHuOE7xFFE9kEOKZcM_KWvOYI5cyMQQJhX4mH_G5-HKUUzRZA-KuviM2QUWgoEgXfZ7piCJlG5CtDj9VGJi4ZpCRKSGClMV542QQ_iugBqqIB2rItnCYZKdKBhaJHzTc5vbKqRfSqJLLAl2SDexrdri2IUk3bocSdSip-dCPQg",
    #     'Content-type': 'application/json'
    # }
    # #print(headers)
    # response = requests.post(endpoint, headers=headers)
    # print(response)
    # print(response.text)

    authority_url = "https://login.microsoftonline.com/" + tenant_name

    scope = ["https://analysis.windows.net/powerbi/api/.default"]

    app = msal.ConfidentialClientApplication(
        id_cliente, authority=authority_url, client_credential=secret)
    result = app.acquire_token_for_client(scopes=scope)
    # print(result['access_token'])

    access_token = result['access_token']

    # authority_url = "https://login.microsoftonline.com/" + id_tenant + "/oauth2/token"
    # payload_token = 'grant_type=client_credentials&code=' + access_token + \
    #     '&client_id=45c839e9-c9c1-422a-ab27-f19bc828f1ea&client_secret=K3U8Q~KMBTwvtKBhKxGLk52wU5mPLzbx5D-zUaF1'
    # response_access = requests.post(url=authority_url)
    # print(response_access)
    authority_url = "https://login.microsoftonline.com/" + id_tenant + "/oauth2/token"
    payload_token = 'grant_type=client_credentials&client_id=45c839e9-c9c1-422a-ab27-f19bc828f1ea&client_secret=K3U8Q~KMBTwvtKBhKxGLk52wU5mPLzbx5D-zUaF1&resource=https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi'
    response_token = requests.post(authority_url, data=payload_token)
    response_data = response_token.json()
    print(response_token.text)
    access_token = response_data["access_token"]
    print(response_token.text)
    header = {'Content-Type': 'application/json',
              'Authorization': f'Bearer {access_token}'}
    refresh_dataset_url = "https://api.powerbi.com/v1.0/myorg/groups/" + \
        id_workspace + "/datasets/" + id_dataset + "/refreshes?$top=1"

    api_call = requests.post(url=refresh_dataset_url, headers=header)
    print(api_call)
    print(api_call.json())
    # result = api_call.json()['value']

    # df = pd.DataFrame(result, columns=[
    #                     'requestId', 'id', 'refreshType', 'startTime', 'endTime', 'status'])
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


lambda_handler(1, 1)
