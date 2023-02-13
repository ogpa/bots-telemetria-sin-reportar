import requests
from funciones_hunter_pro.extraer_datos_session import extraer_datos_session
import json
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

def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto

def abrir_reportes(l):
    # l = cookie_asp,rurl_Login,aspx_Login
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
    
    # 74 = No transmisión de datos

    nombre_reporte = "NoTransmisionPy"
    payload_RunReport = "reportTypeId=74&isDistyView=false&allowSchedule=True&Name=" + nombre_reporte + "&OperatorControlUnitTagName=UnitTag&UnitTagName_Required=selected&UnitTag-rule-number=00&UnitTag-radio-00=1&UnitTag-rule-type-00=unitpicker&UnitTag-rule-input-type-00=picker&UnitTagRuleInput00HTMLNAME_input=Todos+los+veh%C3%ADculos&UnitTagRuleInput00HTMLNAME_selected=-1&UnitTagRuleInput00HTMLNAME_groupselected=&UnitTagRuleInput00HTMLNAME_SingleSelect=False&UnitTagRuleInput00HTMLNAME_AllowSelectAll=True&UnitTagRuleInput00HTMLNAME_GroupSingleSelect=False&UnitTagRuleInput00HTMLNAME_IsGroupOnly=False&UnitTagRuleInput00HTMLNAME_MetabaseEntityTypeId=0&UnitTagRuleInput00HTMLNAME_Context=&UnitTagRuleInput00HTMLNAME_dirty=true&UnitTagRuleInput00HTMLNAME_loadedempty=false&UnitTagRuleInput00HTMLNAME_disabledItems=&UnitTagRuleInput00HTMLNAME_disabledGroupItems=&UnitTagRuleInput00HTMLNAME_groupSelectorsIndividual=False&UnitTagRuleInput00HTMLNAME_pickerTypeId=UnitPicker&UnitTagRuleInput00HTMLNAME_MaxSelectedItemCount=-1&UnitTagRuleInput00HTMLNAME_RefreshType=Unit&UnitTagRuleInput00HTMLNAME_CompanyId=&UnitTagRuleInput00HTMLNAME_GroupByCompany=False&UnitTagRuleInput00HTMLNAME_ApplyExcludedUnit=False&UnitTagRuleInput00HTMLNAME_ExcludedUnitId=0&UnitTagRuleInput00HTMLNAME_IsDistyView=False&UnitTagRuleInput00HTMLNAME_AllowSelectAll=True&UnitTagRuleInput00HTMLNAME_UnitTypeId=0&UnitTagRuleInput00HTMLNAME_HideGroupSelectors=False&UnitTagRuleInput00HTMLNAME_GroupSelectorsIndividual=False&UnitTagRuleInput00HTMLNAME_search=&UnitTagRuleInput00HTMLNAME_ItemId=-1&UnitTagRuleInput00HTMLNAME_AllowFilter=True&UnitTagRuleInput00HTMLNAME_IsSelected=selected&TimePeriod=0&UnitStatusPickerHTMLNAME_input=Activo&UnitStatusPickerHTMLNAME_selected=1&UnitStatusPickerHTMLNAME_groupselected=&UnitStatusPickerHTMLNAME_SingleSelect=False&UnitStatusPickerHTMLNAME_AllowSelectAll=False&UnitStatusPickerHTMLNAME_GroupSingleSelect=False&UnitStatusPickerHTMLNAME_IsGroupOnly=False&UnitStatusPickerHTMLNAME_MetabaseEntityTypeId=0&UnitStatusPickerHTMLNAME_Context=&UnitStatusPickerHTMLNAME_dirty=true&UnitStatusPickerHTMLNAME_loadedempty=false&UnitStatusPickerHTMLNAME_disabledItems=&UnitStatusPickerHTMLNAME_disabledGroupItems=&UnitStatusPickerHTMLNAME_groupSelectorsIndividual=False&UnitStatusPickerHTMLNAME_pickerTypeId=UnitStatusPicker&UnitStatusPickerHTMLNAME_MaxSelectedItemCount=-1&UnitStatusPickerHTMLNAME_search=&UnitStatusPickerHTMLNAME_ItemId=1&UnitStatusPickerHTMLNAME_AllowFilter=True&UnitStatusPickerHTMLNAME_IsSelected=selected&format=HTML&reporttype=datainterval&aggregate_3=&sequence_3=3&visibility_3=false&entitytypeid_3=-1&customfield_3=false&aggregate_7=&sequence_7=2&visibility_7=true&entitytypeid_7=-1&customfield_7=false&aggregate_2=&sequence_2=0&visibility_2=true&entitytypeid_2=-1&customfield_2=false&aggregate_4=&sequence_4=4&visibility_4=false&entitytypeid_4=-1&customfield_4=false&aggregate_5=&sequence_5=1&visibility_5=true&entitytypeid_5=-1&customfield_5=false&aggregate_8=&sequence_8=99&visibility_8=false&entitytypeid_8=-1&customfield_8=false&aggregate_10=&sequence_10=99&visibility_10=false&entitytypeid_10=-1&customfield_10=false&aggregate_9=&sequence_9=99&visibility_9=false&entitytypeid_9=-1&customfield_9=false&aggregate_11=&sequence_11=99&visibility_11=false&entitytypeid_11=-1&customfield_11=false&SelectedFieldIds=&filter=&AdhocListPageNumber=1&AdhocListSortBy=&jsObjectStorage=report&filter=&ListPageNumber=1&ListSortBy=&jsObjectStorage=report"
    headers_RunReport = {
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

    response_RunReport = requests.request("POST", HUN_URL_RUNREPORT, headers=headers_RunReport, data=payload_RunReport)
    #print(response_RunReport.text)
    #print(response_RunReport.text[2])
    
    response_dict = json.loads(response_RunReport.text)
    id_reporte = str(response_dict["LogId"])
    #print(id_reporte)

    #Generar pestaña reporte

    payload_Html={}
    headers_Html = {
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

    response_Html = requests.request("GET", HUN_URL_HTML + id_reporte, headers=headers_Html, data=payload_Html)

    payload_Json = "sort=&group=&filter="
    headers_Json = {
    'authority': 'huntermonitoreopro.com',
    'accept': '*/*',
    'accept-language': 'en',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': l[1] + "; " + l[2] + "; " + CABECERA_ASPNET + l[0],
    'origin': HUN_URL_BASE,
    'referer': HUN_URL_HTML + id_reporte,
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }

    response_Json = requests.request("POST", HUN_URL_CAB_JSON + id_reporte + HUN_URL_FIN_JSON, headers=headers_Json, data=payload_Json)
    #print(response_Json.text)
    data_dict = json.loads(response_Json.text)
    data = data_dict["Data"]
    for d in data:
        print(d["Vehículo"])
        print(d["Ultimosdatosrecibidos"])
        print(d["LatitudLongitud"])

    #return cookie_asp

#login_hunter_pro()