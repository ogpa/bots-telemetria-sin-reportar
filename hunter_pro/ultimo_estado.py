import requests
import json
from funciones_hunter_pro.extraer_datos_session import extraer_datos_session
from fecha_hoy_hunter_pro import fecha_hoy_hunter_pro
import pandas as pd

HUN_URL_BASE = "http://www.huntermonitoreopro.com"
HUN_URL_LOGIN = "https://huntermonitoreopro.com/Account/LogOn?"
HUN_URL_LOGINV3 ="https://huntermonitoreopro.com/Account/LogOnV3/?DistyLanguageOptionId=82"
HUN_URL_CONFIG = "https://huntermonitoreopro.com/Config?returnurl="
HUN_URL_LIVE = "https://huntermonitoreopro.com/live/"
HUN_URL_REPORT = "https://huntermonitoreopro.com/report/"
HUN_URL_RUNREPORT = "https://huntermonitoreopro.com/Report/RunReport/"
HUN_URL_HTML = "https://huntermonitoreopro.com/Report/HTMLReportScheduleLogResult/"
HUN_URL_CAB_JSON = "https://huntermonitoreopro.com/Report/ReportDataJson/?ReportScheduleRunLogID="
HUN_URL_FIN_JSON = "&TableID=0"
CABECERA_ASPNET = "ASP.NET_SessionId="
FIN_ASPNET = ";"
USUARIO = "20605414410"
CLAVE = "mb504"
lista_usuario = [{"mbrenting.dpizarro","mbrenting2022!"},{"dpizarros","xd"}]


def convertir_coordenadas(string_coordenadas):
    latitud = extraer_texto(string_coordenadas,""," ")
    string_coordenadas = string_coordenadas + "x" # helper
    longitud = extraer_texto(string_coordenadas,"/ ","x")
    return latitud,longitud

def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto

def ultimo_estado(l):
    # l = cookie_asp,rurl_Login,aspx_Login

    lista_alias = []
    lista_placa = []
    lista_ultimoreporte = []
    lista_latitud = []
    lista_longitud = []
    lista_alias_temp = [] #Esto es para el reporte de odometro
    lista_odometro = []
    payload_Report={}
    headers_Report = {
    'authority': 'huntermonitoreopro.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en',
    'cookie': l[1] + "; " + l[2] + "; " + CABECERA_ASPNET + l[0],
    'referer': HUN_URL_LIVE,
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Report = requests.request("GET", HUN_URL_REPORT, headers=headers_Report, data=payload_Report)
    
    #print(response_Report.text)

    #Ultimo estado: Posicion y odometro

    #Deseleccionar check celeste de Vehiculo
    # Ejecutar reporte: No transmisión de datos
    ##################################
    # 74 = No transmisión de datos
    ##################################
    
    nombre_reporte = "NoTransmisionPy"
    payload_RunReport_NoTransmision = "reportTypeId=74&isDistyView=false&allowSchedule=True&Name=" + nombre_reporte + "&OperatorControlUnitTagName=UnitTag&UnitTagName_Required=selected&UnitTag-rule-number=00&UnitTag-radio-00=1&UnitTag-rule-type-00=unitpicker&UnitTag-rule-input-type-00=picker&UnitTagRuleInput00HTMLNAME_input=Todos+los+veh%C3%ADculos&UnitTagRuleInput00HTMLNAME_selected=-1&UnitTagRuleInput00HTMLNAME_groupselected=&UnitTagRuleInput00HTMLNAME_SingleSelect=False&UnitTagRuleInput00HTMLNAME_AllowSelectAll=True&UnitTagRuleInput00HTMLNAME_GroupSingleSelect=False&UnitTagRuleInput00HTMLNAME_IsGroupOnly=False&UnitTagRuleInput00HTMLNAME_MetabaseEntityTypeId=0&UnitTagRuleInput00HTMLNAME_Context=&UnitTagRuleInput00HTMLNAME_dirty=true&UnitTagRuleInput00HTMLNAME_loadedempty=false&UnitTagRuleInput00HTMLNAME_disabledItems=&UnitTagRuleInput00HTMLNAME_disabledGroupItems=&UnitTagRuleInput00HTMLNAME_groupSelectorsIndividual=False&UnitTagRuleInput00HTMLNAME_pickerTypeId=UnitPicker&UnitTagRuleInput00HTMLNAME_MaxSelectedItemCount=-1&UnitTagRuleInput00HTMLNAME_RefreshType=Unit&UnitTagRuleInput00HTMLNAME_CompanyId=&UnitTagRuleInput00HTMLNAME_GroupByCompany=False&UnitTagRuleInput00HTMLNAME_ApplyExcludedUnit=False&UnitTagRuleInput00HTMLNAME_ExcludedUnitId=0&UnitTagRuleInput00HTMLNAME_IsDistyView=False&UnitTagRuleInput00HTMLNAME_AllowSelectAll=True&UnitTagRuleInput00HTMLNAME_UnitTypeId=0&UnitTagRuleInput00HTMLNAME_HideGroupSelectors=False&UnitTagRuleInput00HTMLNAME_GroupSelectorsIndividual=False&UnitTagRuleInput00HTMLNAME_search=&UnitTagRuleInput00HTMLNAME_ItemId=-1&UnitTagRuleInput00HTMLNAME_AllowFilter=True&UnitTagRuleInput00HTMLNAME_IsSelected=selected&TimePeriod=0&UnitStatusPickerHTMLNAME_input=Activo&UnitStatusPickerHTMLNAME_selected=1&UnitStatusPickerHTMLNAME_groupselected=&UnitStatusPickerHTMLNAME_SingleSelect=False&UnitStatusPickerHTMLNAME_AllowSelectAll=False&UnitStatusPickerHTMLNAME_GroupSingleSelect=False&UnitStatusPickerHTMLNAME_IsGroupOnly=False&UnitStatusPickerHTMLNAME_MetabaseEntityTypeId=0&UnitStatusPickerHTMLNAME_Context=&UnitStatusPickerHTMLNAME_dirty=true&UnitStatusPickerHTMLNAME_loadedempty=false&UnitStatusPickerHTMLNAME_disabledItems=&UnitStatusPickerHTMLNAME_disabledGroupItems=&UnitStatusPickerHTMLNAME_groupSelectorsIndividual=False&UnitStatusPickerHTMLNAME_pickerTypeId=UnitStatusPicker&UnitStatusPickerHTMLNAME_MaxSelectedItemCount=-1&UnitStatusPickerHTMLNAME_search=&UnitStatusPickerHTMLNAME_ItemId=1&UnitStatusPickerHTMLNAME_AllowFilter=True&UnitStatusPickerHTMLNAME_IsSelected=selected&format=HTML&reporttype=datainterval&aggregate_3=&sequence_3=3&visibility_3=false&entitytypeid_3=-1&customfield_3=false&aggregate_7=&sequence_7=2&visibility_7=true&entitytypeid_7=-1&customfield_7=false&aggregate_2=&sequence_2=0&visibility_2=true&entitytypeid_2=-1&customfield_2=false&aggregate_4=&sequence_4=4&visibility_4=false&entitytypeid_4=-1&customfield_4=false&aggregate_5=&sequence_5=1&visibility_5=true&entitytypeid_5=-1&customfield_5=false&aggregate_8=&sequence_8=99&visibility_8=false&entitytypeid_8=-1&customfield_8=false&aggregate_10=&sequence_10=99&visibility_10=false&entitytypeid_10=-1&customfield_10=false&aggregate_9=&sequence_9=99&visibility_9=false&entitytypeid_9=-1&customfield_9=false&aggregate_11=&sequence_11=99&visibility_11=false&entitytypeid_11=-1&customfield_11=false&SelectedFieldIds=&filter=&AdhocListPageNumber=1&AdhocListSortBy=&jsObjectStorage=report&filter=&ListPageNumber=1&ListSortBy=&jsObjectStorage=report"
    headers_RunReport_NoTransmision = {
    'authority': 'huntermonitoreopro.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': l[1] + "; " + l[2] + "; " + CABECERA_ASPNET + l[0],
    'origin': HUN_URL_BASE,
    'referer': HUN_URL_REPORT,
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }

    response_RunReport_NoTransmision = requests.request("POST", HUN_URL_RUNREPORT, headers=headers_RunReport_NoTransmision, data=payload_RunReport_NoTransmision)
    #print(response_RunReport.text)
    #print(response_RunReport.text[2])
    
    response_dict_NoTransmision = json.loads(response_RunReport_NoTransmision.text)
    id_reporte_NoTransmision = str(response_dict_NoTransmision["LogId"])
    #print(id_reporte)

    #Generar pestaña reporte

    payload_Html_NoTransmision={}
    headers_Html_NoTransmision = {
    'authority': 'huntermonitoreopro.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en',
    'cookie': l[1] + "; " + l[2] + "; " + CABECERA_ASPNET + l[0],
    'referer': HUN_URL_REPORT,
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Html_NoTransmision = requests.request("GET", HUN_URL_HTML + id_reporte_NoTransmision, headers=headers_Html_NoTransmision, data=payload_Html_NoTransmision)

    payload_Json_NoTransmision = "sort=&group=&filter="
    headers_Json_NoTransmision = {
    'authority': 'huntermonitoreopro.com',
    'accept': '*/*',
    'accept-language': 'en',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': l[1] + "; " + l[2] + "; " + CABECERA_ASPNET + l[0],
    'origin': HUN_URL_BASE,
    'referer': HUN_URL_HTML + id_reporte_NoTransmision,
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }

    response_Json_NoTransmision = requests.request("POST", HUN_URL_CAB_JSON + id_reporte_NoTransmision + HUN_URL_FIN_JSON, headers=headers_Json_NoTransmision, data=payload_Json_NoTransmision)
    #print(response_Json.text)
    data_dict_NoTransmision = json.loads(response_Json_NoTransmision.text)
    data_NoTransmision = data_dict_NoTransmision["Data"]
    for d in data_NoTransmision:
        lista_alias.append(d["Vehículo"])
        lista_ultimoreporte.append(d["Ultimosdatosrecibidos"][:-1])
        c = convertir_coordenadas(d["LatitudLongitud"])
        lista_latitud.append(c[0])
        lista_longitud.append(c[1])

    dict_NoTransmision = {
        "descripcion_vehiculo":lista_alias,
        "ultimo_reporte":lista_ultimoreporte,
        "latitud":lista_latitud,
        "longitud":lista_longitud,
    }

    #return cookie_asp

    # Odómetro en reporte "Kilometraje"
    nombre_reporte = "OdometroPy"

    fechas = fecha_hoy_hunter_pro()
    # fecha[0] = inicio (1 mes atras)
    # fecha[1] = fin (hoy)
    payload_RunReport_Kilometraje = "reportTypeId=2&isDistyView=false&allowSchedule=True&Name=" + nombre_reporte +"&OperatorControlUnitTagName=UnitTag&UnitTagName_Required=selected&UnitTag-rule-number=00&UnitTag-radio-00=1&UnitTag-rule-type-00=unitpicker&UnitTag-rule-input-type-00=picker&UnitTagRuleInput00HTMLNAME_input=Todos+los+veh%C3%ADculos&UnitTagRuleInput00HTMLNAME_selected=-1&UnitTagRuleInput00HTMLNAME_groupselected=&UnitTagRuleInput00HTMLNAME_SingleSelect=False&UnitTagRuleInput00HTMLNAME_AllowSelectAll=True&UnitTagRuleInput00HTMLNAME_GroupSingleSelect=False&UnitTagRuleInput00HTMLNAME_IsGroupOnly=False&UnitTagRuleInput00HTMLNAME_MetabaseEntityTypeId=0&UnitTagRuleInput00HTMLNAME_Context=&UnitTagRuleInput00HTMLNAME_dirty=true&UnitTagRuleInput00HTMLNAME_loadedempty=false&UnitTagRuleInput00HTMLNAME_disabledItems=&UnitTagRuleInput00HTMLNAME_disabledGroupItems=&UnitTagRuleInput00HTMLNAME_groupSelectorsIndividual=False&UnitTagRuleInput00HTMLNAME_pickerTypeId=UnitPicker&UnitTagRuleInput00HTMLNAME_MaxSelectedItemCount=-1&UnitTagRuleInput00HTMLNAME_RefreshType=Unit&UnitTagRuleInput00HTMLNAME_CompanyId=&UnitTagRuleInput00HTMLNAME_GroupByCompany=False&UnitTagRuleInput00HTMLNAME_ApplyExcludedUnit=False&UnitTagRuleInput00HTMLNAME_ExcludedUnitId=0&UnitTagRuleInput00HTMLNAME_IsDistyView=False&UnitTagRuleInput00HTMLNAME_AllowSelectAll=True&UnitTagRuleInput00HTMLNAME_UnitTypeId=0&UnitTagRuleInput00HTMLNAME_HideGroupSelectors=False&UnitTagRuleInput00HTMLNAME_GroupSelectorsIndividual=False&UnitTagRuleInput00HTMLNAME_search=&UnitTagRuleInput00HTMLNAME_ItemId=-1&UnitTagRuleInput00HTMLNAME_AllowFilter=True&UnitTagRuleInput00HTMLNAME_IsSelected=selected&startdate="+ fechas[0] +"+00%3A00&enddate=" + fechas[1] + "+23%3A59&source=1&format=HTML&reporttype=mileage&aggregate_2=&sequence_2=0&visibility_2=true&entitytypeid_2=-1&customfield_2=false&aggregate_6=&sequence_6=6&visibility_6=false&entitytypeid_6=-1&customfield_6=false&aggregate_7=&sequence_7=7&visibility_7=false&entitytypeid_7=-1&customfield_7=false&aggregate_3=&sequence_3=3&visibility_3=false&entitytypeid_3=-1&customfield_3=false&aggregate_4=&sequence_4=4&visibility_4=false&entitytypeid_4=-1&customfield_4=false&aggregate_5=max&sequence_5=1&visibility_5=true&entitytypeid_5=-1&customfield_5=false&prop_summarize=false&SelectedFieldIds=&filter=&AdhocListPageNumber=1&AdhocListSortBy=&jsObjectStorage=report&filter=&ListPageNumber=1&ListSortBy=&jsObjectStorage=report"
    headers_RunReport_Kilometraje = {
    'authority': 'huntermonitoreopro.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie':  l[1] + "; " + l[2] + "; " + CABECERA_ASPNET + l[0],
    'origin': HUN_URL_BASE,
    'referer': HUN_URL_REPORT,
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }

    response_RunReport_Kilometraje = requests.request("POST", HUN_URL_RUNREPORT, headers=headers_RunReport_Kilometraje, data=payload_RunReport_Kilometraje)
    #print(response_RunReport.text)
    #print(response_RunReport.text[2])
    
    response_dict_Kilometraje = json.loads(response_RunReport_Kilometraje.text)
    id_reporte_Kilometraje = str(response_dict_Kilometraje["LogId"])
    #print(id_reporte)

    #Generar pestaña reporte

    payload_Html_Kilometraje={}
    headers_Html_Kilometraje = {
    'authority': 'huntermonitoreopro.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en',
    'cookie': l[1] + "; " + l[2] + "; " + CABECERA_ASPNET + l[0],
    'referer': HUN_URL_REPORT,
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Html_Kilometraje = requests.request("GET", HUN_URL_HTML + id_reporte_Kilometraje, headers=headers_Html_Kilometraje, data=payload_Html_Kilometraje)

    payload_Json_Kilometraje = "sort=&group=&filter="
    headers_Json_Kilometraje = {
    'authority': 'huntermonitoreopro.com',
    'accept': '*/*',
    'accept-language': 'en',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': l[1] + "; " + l[2] + "; " + CABECERA_ASPNET + l[0],
    'origin': HUN_URL_BASE,
    'referer': HUN_URL_HTML + id_reporte_Kilometraje,
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }

    response_Json_Kilometraje = requests.request("POST", HUN_URL_CAB_JSON + id_reporte_Kilometraje + HUN_URL_FIN_JSON, headers=headers_Json_Kilometraje, data=payload_Json_Kilometraje)
    #print(response_Json.text)
    data_dict_Kilometraje = json.loads(response_Json_Kilometraje.text)
    data_Kilometraje = data_dict_Kilometraje["Data"]
    for d in data_Kilometraje:
        lista_alias_temp.append(d["Vehículo"])
        lista_odometro.append(d["Odómetrofinal"])

    dict_Kilometraje = {
        "descripcion_vehiculo": lista_alias_temp,
        "odometro":lista_odometro
    }
    #print(dict_NoTransmision)
    df_NoTransmision = pd.DataFrame(dict_NoTransmision)
    df_Kilometraje = pd.DataFrame(dict_Kilometraje)
    df_ultimo_estado = pd.merge(df_NoTransmision,df_Kilometraje,on="alias")
    #print(df_ultimo_estado)
    return df_ultimo_estado
#login_hunter_pro()