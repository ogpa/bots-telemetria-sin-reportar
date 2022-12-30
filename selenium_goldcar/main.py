from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import requests
import urllib
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.action_chains import ActionChains
GOLD_URL_LOGIN = "http://gpsenperu.gpsgoldcar.com/"


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    # empieza a buscar el fin a partir del inicio
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


chrome_options = Options()
prefs = {"download.default_directory": os.getcwd()}
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(GOLD_URL_LOGIN)
print(driver.title)

usuario = driver.find_element(By.ID, "user")
usuario.send_keys("mbrenting")

password = driver.find_element(By.ID, "passw")
password.send_keys("mbrenting2021")
# driver.save_screenshot("completar_registro.png")
driver.find_element(By.NAME, "submit").click()
# driver.save_screenshot("submit.png")
# boton_reportes = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="hb_mi_reports_ctl"]/div/div')))
# boton_reportes.click()

boton_add_object = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="report_templates_filter_target"]/div/div[1]/div[2]/div[2]/div[2]/button')))
boton_add_object.click()

boton_dropdown = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="report_templates_filter_reports"]')))
boton_dropdown.click()

boton_horas_trabajadas = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="report_templates_filter_target"]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/ul/li[3]/div')))
boton_horas_trabajadas.click()
all_cookies = driver.get_cookies()
cookies_dict = {}
for cookie in all_cookies:
    cookies_dict[cookie['name']] = cookie['value']
print(cookies_dict)

# select = Select(driver.find_element("id", 'report_templates_filter_reports'))
# select.select_by_visible_text('Horas Trabajadas MB Renting')

boton_yesterday = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="report_templates_filter_time-yesterday-label"]')))
boton_yesterday.click()


# boton_panel = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
#     (By.XPATH, '//*[@id="dPanel-center"]')))
# boton_panel.click()

driver.save_screenshot("panel.png")


time.sleep(5)
# element_export = driver.find_element(
#     By.CSS_SELECTOR, '//*[@id="report_result_export"]')
# #driver.execute_script("$(arguments[0]).click();", element)
# driver.execute_script("arguments[0].click();", element_export)
# element_export = driver.find_element(
# By.XPATH, '//*[@id="report_result_export"]')
# action = ActionChains(driver)
# action.move_to_element(element_export).click().perform()
all_cookies = driver.get_cookies()
cookies_dict = {}
for cookie in all_cookies:
    cookies_dict[cookie['name']] = cookie['value']
print(cookies_dict)

html_source = driver.page_source
scrape_filename = "goldcar.html"
# with open(scrape_filename, "w", encoding="utf-8") as f:  # Descomentar para hacer primer request
#     f.write(html_source)  # Descomentar para hacer primer request
a = extraer_texto(html_source, '<img class="olTileImage" src="https://hst-api.wialon.com/',
                  '.png" style="visibility: inherit; opacity: 1; position: absolute;')
sid = a[-32:]
print("Horas trabajadas")
print(sid)
url_Excel = "https://hst-api.wialon.com/wialon/ajax.html?sid=" + sid + '&svc=report/export_result&params=%7B%22attachMap%22%3A1%2C%22extendBounds%22%3A0%2C%22compress%22%3A0%2C%22delimiter%22%3A%22semicolon%22%2C%22outputFileName%22%3A%22MB_Renting_%5BAntapaccay%5D_Horas_Trabajadas_MB_Renting_2022-12-29_16-09-30%22%2C%22pageOrientation%22%3A%22landscap%22%2C%22pageSize%22%3A%22a4%22%2C%22pageWidth%22%3A%220%22%2C%22format%22%3A8%7D'
payload_Excel = {}
headers_Excel = {
    'authority': 'hst-api.wialon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'http://gpsenperu.gpsgoldcar.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response_Excel = requests.request(
    "GET", url_Excel, headers=headers_Excel, data=payload_Excel)
open("Horas_Trabajadas.xlsx", "wb").write(response_Excel.content)
# print(a[-32:])

boton_dropdown = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="report_templates_filter_reports"]')))
boton_dropdown.click()

boton_kilometraje_horas = driver.find_element(
    By.XPATH, '//*[@id="report_templates_filter_target"]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/div')

# boton_kilometraje_horas = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
#     (By.XPATH, '//*[@id="report_templates_filter_target"]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/div')))
boton_kilometraje_horas.click()
all_cookies = driver.get_cookies()
cookies_dict = {}
for cookie in all_cookies:
    cookies_dict[cookie['name']] = cookie['value']
print(cookies_dict)

# select = Select(driver.find_element("id", 'report_templates_filter_reports'))
# select.select_by_visible_text('Horas Trabajadas MB Renting')

boton_yesterday = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="report_templates_filter_time-yesterday-label"]')))
boton_yesterday.click()
time.sleep(5)

all_cookies = driver.get_cookies()
cookies_dict = {}
for cookie in all_cookies:
    cookies_dict[cookie['name']] = cookie['value']
print(cookies_dict)

html_kilometraje_horas = driver.page_source
a = extraer_texto(html_kilometraje_horas, '<img class="olTileImage" src="https://hst-api.wialon.com/',
                  '.png" style="visibility: inherit; opacity: 1; position: absolute;')
sid_kilometraje_horas = a[-32:]
print("sid Kilometraje Horas")
print(sid_kilometraje_horas)
url_Kilometraje_Horas = "https://hst-api.wialon.com/wialon/ajax.html?sid=" + sid + '&svc=report/export_result&params=%7B%22attachMap%22%3A1%2C%22extendBounds%22%3A0%2C%22compress%22%3A0%2C%22delimiter%22%3A%22semicolon%22%2C%22outputFileName%22%3A%22MB_Renting_%5BAntapaccay%5D_Horas_Trabajadas_MB_Renting_2022-12-29_16-09-30%22%2C%22pageOrientation%22%3A%22landscap%22%2C%22pageSize%22%3A%22a4%22%2C%22pageWidth%22%3A%220%22%2C%22format%22%3A8%7D'
payload_Kilometraje_Horas = {}
headers_Kilometraje_Horas = {
    'authority': 'hst-api.wialon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'http://gpsenperu.gpsgoldcar.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response_Kilometraje_Horas = requests.request(
    "GET", url_Kilometraje_Horas, headers=headers_Kilometraje_Horas, data=payload_Kilometraje_Horas)
open("Kilometraje_Horas.xlsx", "wb").write(response_Kilometraje_Horas.content)

# boton_panel = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
#     (By.XPATH, '//*[@id="dPanel-center"]')))
# boton_panel.click()

# print(html_source)

# boton_export = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
#     (By.XPATH, '//*[@id="report_result_export"]/div')))
# boton_export.click()
# driver.save_screenshot("export.png")
# element_excel = driver.find_element(
#     By.XPATH, '//*[@id="report_result_export"]/div/div/div[1]')
# #driver.execute_script("$(arguments[0]).click();", element)
# driver.execute_script("arguments[0].click();", element_excel)
# driver.save_screenshot("excel.png")
# boton_excel = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
#     (By.XPATH, '//*[@id="report_result_export"]/div/div/div[1]')))
# boton_excel.click()
