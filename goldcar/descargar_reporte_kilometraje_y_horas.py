import requests


GOLD_URL_BASE_GOLDCAR = "http://gpsenperu.gpsgoldcar.com/"


def descargar_reporte_kilometraje_y_horas(sid):

    # Click Descargar XLSX
    nombreArchivo_Goldcar_local = "Kilometraje_y_Horas_Goldcar.xlsx"

    url_Descargar_XLSX = 'https://hst-api.wialon.com/wialon/ajax.html?sid=' + sid + \
        '&svc=report/export_result&params=%7B%22attachMap%22%3A1%2C%22extendBounds%22%3A0%2C%22compress%22%3A0%2C%22delimiter%22%3A%22semicolon%22%2C%22outputFileName%22%3A%22' + \
        nombreArchivo_Goldcar_local + \
        '%22%2C%22pageOrientation%22%3A%22landscap%22%2C%22pageSize%22%3A%22a4%22%2C%22pageWidth%22%3A%220%22%2C%22format%22%3A8%7D"'

    payload_Descargar_XLSX = {}
    headers_Descargar_XLSX = {
        'authority': 'hst-api.wialon.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'referer': GOLD_URL_BASE_GOLDCAR,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Descargar_XLSX = requests.request(
        "GET", url_Descargar_XLSX, headers=headers_Descargar_XLSX, data=payload_Descargar_XLSX)

    open(nombreArchivo_Goldcar_local, "wb").write(
        response_Descargar_XLSX.content)
    return nombreArchivo_Goldcar_local
