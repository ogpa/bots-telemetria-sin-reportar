import requests
import time
from datetime import datetime, timedelta
import pytz

GOLD_URL_WIALON = "https://hst-api.wialon.com"
GOLD_URL_WIALON_POST = "https://hst-api.wialon.com/wialon/post.html"


def epoch():
    epoch = int(time.time())
    return epoch


def epoch_hoy():
    tz_Lima = pytz.timezone('America/Lima')
    tiempo_Lima = datetime.now(tz_Lima)

    hora_inicio_Lima = datetime(tiempo_Lima.year, tiempo_Lima.month,
                                tiempo_Lima.day)
    hora_fin_Lima = datetime(tiempo_Lima.year, tiempo_Lima.month,
                             tiempo_Lima.day) + timedelta(days=1) - timedelta(seconds=1)
    hora_inicio_str = str(int(hora_inicio_Lima.timestamp()))
    hora_fin_str = str(int(hora_fin_Lima.timestamp()))
    return hora_inicio_str, hora_fin_str


def generar_reporte_horas_trabajadas(periodo, sid):

    # Click Dropdown Reporte "Horas Trabajdas MB Renting"

    url_Seleccionar_Horas_Trabajadas = "https://hst-api.wialon.com/wialon/ajax.html?svc=report/get_report_data&sid=" + sid
    payload_Seleccionar_Horas_Trabajadas = 'params=%7B%22itemId%22%3A25005170%2C%22col%22%3A%5B2%5D%2C%22flags%22%3A0%7D&sid=' + sid
    headers_Seleccionar_Horas_Trabajadas = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': GOLD_URL_WIALON,
        'referer': GOLD_URL_WIALON_POST,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Seleccionar_Horas_Trabajadas = requests.request("POST", url_Seleccionar_Horas_Trabajadas,
                                                             headers=headers_Seleccionar_Horas_Trabajadas, data=payload_Seleccionar_Horas_Trabajadas)

    # Click Ejecutar ayer
    url_Batch = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/batch&sid=" + sid

    payload_Batch = 'params=%7B%22params%22%3A%5B%7B%22svc%22%3A%22report%2Fget_report_data%22%2C%22params%22%3A%7B%22itemId%22%3A25005170%2C%22col%22%3A%5B%222%22%5D%2C%22flags%22%3A0%7D%7D%5D%2C%22flags%22%3A0%7D&sid=' + sid
    headers_Batch = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': GOLD_URL_WIALON,
        'referer': GOLD_URL_WIALON_POST,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Batch = requests.request(
        "POST", url_Batch, headers=headers_Batch, data=payload_Batch)

    # Estoy omitiendo el write log

    url_Write_Log = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/write_log&sid=" + sid
    tiempo_epoch = str(epoch())
    payload_Write_Log = 'params=%7B%22table%22%3A%22front_stats%22%2C%22stat%22%3A%7B%22feature_type%22%3A4469%2C%22action_type%22%3A446901%2C%22stat_value%22%3A%22%7B%5C%22module%5C%22%3A%5C%22%D0%9E%D1%82%D1%87%D0%B5%D1%82%D1%8B%5C%22%2C%5C%22period%5C%22%3A-86399%2C%5C%22periodType%5C%22%3A%5C%22%D0%91%D1%8B%D1%81%D1%82%D1%80%D1%8B%D0%B9%20%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4%5C%22%2C%5C%22currentInterval%5C%22%3Anull%2C%5C%22datePickerWasClicked%5C%22%3Anull%7D%22%2C%22time%22%3A' + \
        tiempo_epoch + '%2C%22service_id%22%3A13281579%2C%22service_name%22%3A%22ccardenas%22%2C%22user_id%22%3A22630230%2C%22user_name%22%3A%22mbrenting%22%2C%22account_id%22%3A17084371%2C%22account_name%22%3A%22%22%2C%22unit_id%22%3A0%2C%22unit_name%22%3A%22%22%2C%22count%22%3A0%2C%22duration%22%3A0%7D%7D&sid=' + sid
    headers_Write_Log = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': GOLD_URL_WIALON,
        'referer': GOLD_URL_WIALON_POST,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Write_Log = requests.request(
        "POST", url_Write_Log, headers=headers_Write_Log, data=payload_Write_Log)

    url_Exec_Report = "https://hst-api.wialon.com/wialon/ajax.html?svc=report/exec_report&sid=" + sid

    if periodo == "Hoy":
        fecha_unix = epoch_hoy()  # Ayer, Hoy
        valor_from = fecha_unix[0]
        valor_to = fecha_unix[1]
        payload_Exec_Report = "params=%7B%22reportResourceId%22%3A25005170%2C%22reportTemplateId%22%3A2%2C%22reportTemplate%22%3Anull%2C%22reportObjectId%22%3A25676298%2C%22reportObjectSecId%22%3A0%2C%22interval%22%3A%7B%22flags%22%3A16777216%2C%22from%22%3A" + \
            valor_from + "%2C%22to%22%3A" + valor_to + \
            "%7D%2C%22remoteExec%22%3A1%2C%22reportObjectIdList%22%3A%5B23151123%5D%7D&sid=" + sid
    elif periodo == "Ayer":
        valor_from = "0"
        valor_to = "1"
        payload_Exec_Report = 'params=%7B%22reportResourceId%22%3A25005170%2C%22reportTemplateId%22%3A2%2C%22reportTemplate%22%3Anull%2C%22reportObjectId%22%3A25676298%2C%22reportObjectSecId%22%3A0%2C%22interval%22%3A%7B%22from%22%3A' + \
            valor_from + '%2C%22to%22%3A' + valor_to + \
            '%2C%22flags%22%3A16777218%7D%2C%22remoteExec%22%3A1%2C%22reportObjectIdList%22%3A%5B23151123%5D%7D&sid=' + sid
    # Qué es exactamente "flags"?
    # Tener en cuenta a "reportObjectIdList"

    headers_Exec_Report = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': GOLD_URL_WIALON,
        'referer': GOLD_URL_WIALON_POST,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Exec_Report = requests.request(
        "POST", url_Exec_Report, headers=headers_Exec_Report, data=payload_Exec_Report)

    # Get Report Status debe ejecutarse hasta que la respuesta sea {"status":"4"}

    url_Get_Report_Status = "https://hst-api.wialon.com/wialon/ajax.html?svc=report/get_report_status&sid=" + sid

    payload_Get_Report_Status = 'params=%7B%7D&sid=' + sid
    headers_Get_Report_Status = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': GOLD_URL_WIALON,
        'referer': GOLD_URL_WIALON_POST,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Get_Report_Status = requests.request(
        "POST", url_Get_Report_Status, headers=headers_Get_Report_Status, data=payload_Get_Report_Status)

    time.sleep(6)
    url_Get_Report_Status = "https://hst-api.wialon.com/wialon/ajax.html?svc=report/get_report_status&sid=" + sid

    payload_Get_Report_Status = 'params=%7B%7D&sid=' + sid
    headers_Get_Report_Status = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': GOLD_URL_WIALON,
        'referer': GOLD_URL_WIALON_POST,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Get_Report_Status = requests.request(
        "POST", url_Get_Report_Status, headers=headers_Get_Report_Status, data=payload_Get_Report_Status)

    url_Apply_Report_Result = "https://hst-api.wialon.com/wialon/ajax.html?svc=report/apply_report_result&sid=" + sid

    payload_Apply_Report_Result = 'params=%7B%7D&sid=' + sid
    headers_Apply_Report_Result = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': GOLD_URL_WIALON,
        'referer': GOLD_URL_WIALON_POST,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    response_Apply_Report_Result = requests.request(
        "POST", url_Apply_Report_Result, headers=headers_Apply_Report_Result, data=payload_Apply_Report_Result)

    url_Select_Result_Rows = "https://hst-api.wialon.com/wialon/ajax.html?svc=report/select_result_rows&sid=" + sid

    payload_Select_Result_Rows = 'params=%7B%22tableIndex%22%3A0%2C%22config%22%3A%7B%22type%22%3A%22range%22%2C%22data%22%3A%7B%22from%22%3A0%2C%22to%22%3A49%2C%22level%22%3A0%2C%22unitInfo%22%3A1%7D%7D%7D&sid=' + sid
    headers_Select_Result_Rows = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': GOLD_URL_WIALON,
        'referer': GOLD_URL_WIALON_POST,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Select_Result_Rows = requests.request(
        "POST", url_Select_Result_Rows, headers=headers_Select_Result_Rows, data=payload_Select_Result_Rows)
