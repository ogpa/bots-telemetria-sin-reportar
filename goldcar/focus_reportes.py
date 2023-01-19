import requests
import time


GOLD_URL_WIALON = "https://hst-api.wialon.com"
GOLD_URL_WIALON_POST = "https://hst-api.wialon.com/wialon/post.html"


def epoch():
    epoch = int(time.time())
    return epoch


def focus_reportes(sid):
    url_Write_1 = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/write_log&sid=" + sid
    tiempo_epoch = str(epoch())
    payload_Write_1 = 'params=%7B%22table%22%3A%22front_stats%22%2C%22stat%22%3A%7B%22feature_type%22%3A5189%2C%22action_type%22%3A518901%2C%22stat_value%22%3A%22Monitoring-Reports%22%2C%22time%22%3A' + tiempo_epoch + \
        '%2C%22service_id%22%3A13281579%2C%22service_name%22%3A%22ccardenas%22%2C%22user_id%22%3A22630230%2C%22user_name%22%3A%22mbrenting%22%2C%22account_id%22%3A17084371%2C%22account_name%22%3A%22%22%2C%22unit_id%22%3A0%2C%22unit_name%22%3A%22%22%2C%22count%22%3A0%2C%22duration%22%3A0%7D%7D&sid=' + sid
    headers_Write_1 = {
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
    response_Write_1 = requests.request(
        "POST", url_Write_1, headers=headers_Write_1, data=payload_Write_1)

    url_Write_2 = url_Write_1
    payload_Write_2 = 'params=%7B%22table%22%3A%22front_stats%22%2C%22stat%22%3A%7B%22feature_type%22%3A5189%2C%22action_type%22%3A518902%2C%22stat_value%22%3A%22Monitoring%22%2C%22duration%22%3A59349%2C%22time%22%3A'+tiempo_epoch + \
        '%2C%22service_id%22%3A13281579%2C%22service_name%22%3A%22ccardenas%22%2C%22user_id%22%3A22630230%2C%22user_name%22%3A%22mbrenting%22%2C%22account_id%22%3A17084371%2C%22account_name%22%3A%22%22%2C%22unit_id%22%3A0%2C%22unit_name%22%3A%22%22%2C%22count%22%3A0%7D%7D&sid=' + sid
    headers_Write_2 = {
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
    response_Write_2 = requests.request(
        "POST", url_Write_2, headers=headers_Write_2, data=payload_Write_2)

    url_Batch = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/batch&sid=" + sid
    payload_Batch = 'params=%7B%22params%22%3A%5B%7B%22svc%22%3A%22core%2Fupdate_data_flags%22%2C%22params%22%3A%7B%22spec%22%3A%5B%7B%22type%22%3A%22type%22%2C%22data%22%3A%22avl_resource%22%2C%22flags%22%3A8197%2C%22mode%22%3A1%7D%5D%7D%7D%5D%2C%22flags%22%3A0%7D&sid=' + sid
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

    reponse_Batch = requests.request(
        "POST", url_Batch, headers=headers_Batch, data=payload_Batch)

    url_Get_Report_Data = "https://hst-api.wialon.com/wialon/ajax.html?svc=report/get_report_data&sid=" + sid
    payload_Get_Report_Data = 'params=%7B%22itemId%22%3A25005170%2C%22col%22%3A%5B9%5D%2C%22flags%22%3A0%7D&sid=' + sid
    headers_Get_Report_Data = {
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
    response_Get_Report_Data = requests.request(
        "POST", url_Get_Report_Data, headers=headers_Get_Report_Data, data=payload_Get_Report_Data)

    url_Search_Items = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_items&sid=" + sid
    payload_Search_Items = 'params=%7B%22spec%22%3A%7B%22itemsType%22%3A%22avl_resource%22%2C%22propName%22%3A%22sys_name%22%2C%22propValueMask%22%3A%22*%22%2C%22sortType%22%3A%22%22%7D%2C%22force%22%3A1%2C%22flags%22%3A5%2C%22from%22%3A0%2C%22to%22%3A4294967295%7D&sid=' + sid
    headers_Search_Items = {
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
    response_Search_Items = requests.request(
        "POST", url_Search_Items, headers=headers_Search_Items, data=payload_Search_Items)

    url_Update_1 = "https://hst-api.wialon.com/wialon/ajax.html?svc=item/update_custom_property&sid=" + sid
    payload_Update_1 = 'params=%7B%22itemId%22%3A22630230%2C%22name%22%3A%22hpnl%22%2C%22value%22%3A%22hb_mi_reports_ctl%22%7D&sid=' + sid
    headers_Update_1 = {
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
    response_Update_1 = requests.request(
        "POST", url_Update_1, headers=headers_Update_1, data=payload_Update_1)

    url_Update_2 = url_Update_1
    payload_Update_2 = 'params=%7B%22itemId%22%3A22630230%2C%22name%22%3A%22fpnl%22%2C%22value%22%3A%22report_templates_filter_target%22%7D&sid=' + sid
    headers_Update_2 = {
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
    response_Update_2 = requests.request(
        "POST", url_Update_2, headers=headers_Update_2, data=payload_Update_2)
