import requests
import json
from hunter_pro.funciones_hunter_pro.extraer_datos_session import extraer_datos_session
from hunter_pro.fecha_ayer_hunter_pro import fecha_ayer_hunter_pro

import pandas as pd
from datetime import datetime, timedelta

HUN_URL_BASE = "http://www.huntermonitoreopro.com"
HUN_URL_LOGIN = "https://huntermonitoreopro.com/Account/LogOn?"
HUN_URL_LOGINV3 = "https://huntermonitoreopro.com/Account/LogOnV3/?DistyLanguageOptionId=82"
HUN_URL_CONFIG = "https://huntermonitoreopro.com/Config?returnurl="
HUN_URL_LIVE = "https://huntermonitoreopro.com/live/"
HUN_URL_REPORT = "https://huntermonitoreopro.com/report/"
HUN_URL_RUNREPORT = "https://huntermonitoreopro.com/Report/RunReport/"
HUN_URL_HTML = "https://huntermonitoreopro.com/Report/HTMLReportScheduleLogResult/"
HUN_URL_CAB_JSON = "https://huntermonitoreopro.com/Report/ReportDataJson/?ReportScheduleRunLogID="
HUN_URL_FIN_JSON = "&TableID=0"
CABECERA_ASPNET = "ASP.NET_SessionId="
FIN_ASPNET = ";"

lista_usuario = [{"mbrenting.dpizarro", "mbrenting2022!"}, {"dpizarros", "xd"}]


def convertir_coordenadas(string_coordenadas):
    latitud = extraer_texto(string_coordenadas, "", " ")
    string_coordenadas = string_coordenadas + "x"  # helper
    longitud = extraer_texto(string_coordenadas, "/ ", "x")
    return latitud, longitud


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def fecha(delta):
    d = datetime.today() - timedelta(days=delta)
    fecha_yyyymmdd = d.strftime("%Y%m%d")
    fecha_ddmmyyyy = d.strftime("%d/%m/%Y")
    return fecha_yyyymmdd, fecha_ddmmyyyy


def calcular_porcentaje_ralenti(duracion, duracion_ralenti):

    if (duracion_ralenti == 0) or (duracion_ralenti == "") or (duracion_ralenti == "0") or (duracion_ralenti == "0.00"):
        porcentaje_ralenti = 0
    else:
        porcentaje_ralenti = (
            int(duracion_ralenti)/(int(duracion)+int(duracion_ralenti)))
    return porcentaje_ralenti


def convertir_placa(alias):
    c = "-"
    pos_guion = alias.find(c)
    if pos_guion != -1:
        placa = alias[pos_guion-3:pos_guion+4]
    else:
        placa = alias
    return placa


def productividad(l, hora_reporte):
    # l = cookie_asp,rurl_Login,aspx_Login

    lista_alias = []
    lista_placa = []
    lista_velocidad_maxima = []
    lista_ralenti = []
    lista_conduccion = []
    lista_distancia = []  # Esto es para el reporte de odometro
    lista_porcentaje_ralenti = []
    lista_dias_uso = []
    lista_fecha = []
    lista_proveedor = []
    # print(response_Report.text)

    payload_Report = {}
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

    response_Report = requests.request(
        "GET", HUN_URL_REPORT, headers=headers_Report, data=payload_Report)
    # Ultimo estado: Posicion y odometro

    # Deseleccionar check celeste de Vehiculo
    # Ejecutar reporte: No transmisión de datos
    ##################################
    # 10 = Actividad diaria
    ##################################
    if hora_reporte == "Ayer":
        fecha_payload = fecha(1)  # dd/mm/yyyy
    elif hora_reporte == "Hoy":
        fecha_payload = fecha(0)  # dd/mm/yyyy
    nombre_reporte = "ActividadDiariaPy"
    ayer = fecha_ayer_hunter_pro()
    payload_RunReport_Productividad = "reportTypeId=10&isDistyView=false&allowSchedule=True&Name=" + nombre_reporte + "&OperatorControlUnitDriverName=UnitDriver&UnitDriverName_Required=selected&UnitDriver-rule-number=00&UnitDriver-radio-00=1&UnitDriver-rule-type-00=unitpicker&UnitDriver-rule-input-type-00=picker&UnitDriverRuleInput00HTMLNAME_input=Todos+los+veh%C3%ADculos&UnitDriverRuleInput00HTMLNAME_selected=-1&UnitDriverRuleInput00HTMLNAME_groupselected=&UnitDriverRuleInput00HTMLNAME_SingleSelect=False&UnitDriverRuleInput00HTMLNAME_AllowSelectAll=True&UnitDriverRuleInput00HTMLNAME_GroupSingleSelect=False&UnitDriverRuleInput00HTMLNAME_IsGroupOnly=False&UnitDriverRuleInput00HTMLNAME_MetabaseEntityTypeId=0&UnitDriverRuleInput00HTMLNAME_Context=&UnitDriverRuleInput00HTMLNAME_dirty=true&UnitDriverRuleInput00HTMLNAME_loadedempty=false&UnitDriverRuleInput00HTMLNAME_disabledItems=&UnitDriverRuleInput00HTMLNAME_disabledGroupItems=&UnitDriverRuleInput00HTMLNAME_groupSelectorsIndividual=False&UnitDriverRuleInput00HTMLNAME_pickerTypeId=UnitPicker&UnitDriverRuleInput00HTMLNAME_MaxSelectedItemCount=-1&UnitDriverRuleInput00HTMLNAME_RefreshType=Unit&UnitDriverRuleInput00HTMLNAME_CompanyId=&UnitDriverRuleInput00HTMLNAME_GroupByCompany=False&UnitDriverRuleInput00HTMLNAME_ApplyExcludedUnit=False&UnitDriverRuleInput00HTMLNAME_ExcludedUnitId=0&UnitDriverRuleInput00HTMLNAME_IsDistyView=False&UnitDriverRuleInput00HTMLNAME_AllowSelectAll=True&UnitDriverRuleInput00HTMLNAME_UnitTypeId=0&UnitDriverRuleInput00HTMLNAME_HideGroupSelectors=False&UnitDriverRuleInput00HTMLNAME_GroupSelectorsIndividual=False&UnitDriverRuleInput00HTMLNAME_search=&UnitDriverRuleInput00HTMLNAME_ItemId=-1&UnitDriverRuleInput00HTMLNAME_AllowFilter=True&UnitDriverRuleInput00HTMLNAME_IsSelected=selected&startdate=" + \
        ayer + "+00%3A00&enddate=" + ayer + "+23%3A59&format=HTML&reporttype=detailedactivity&aggregate_5=&sequence_5=4&visibility_5=false&entitytypeid_5=-1&customfield_5=false&aggregate_11=sum&sequence_11=1&visibility_11=true&entitytypeid_11=-1&customfield_11=false&aggregate_6=&sequence_6=5&visibility_6=false&entitytypeid_6=-1&customfield_6=false&aggregate_7=&sequence_7=4&visibility_7=true&entitytypeid_7=-1&customfield_7=false&aggregate_8=&sequence_8=3&visibility_8=true&entitytypeid_8=-1&customfield_8=false&aggregate_9=&sequence_9=8&visibility_9=false&entitytypeid_9=-1&customfield_9=false&aggregate_10=&sequence_10=9&visibility_10=false&entitytypeid_10=-1&customfield_10=false&aggregate_12=&sequence_12=12&visibility_12=false&entitytypeid_12=-1&customfield_12=false&aggregate_13=&sequence_13=2&visibility_13=true&entitytypeid_13=-1&customfield_13=false&aggregate_2=&sequence_2=2&visibility_2=false&entitytypeid_2=-1&customfield_2=false&aggregate_3=&sequence_3=0&visibility_3=true&entitytypeid_3=-1&customfield_3=false&aggregate_4=&sequence_4=3&visibility_4=false&entitytypeid_4=-1&customfield_4=false&aggregate_15=&sequence_15=99&visibility_15=false&entitytypeid_15=-1&customfield_15=false&aggregate_14=&sequence_14=99&visibility_14=false&entitytypeid_14=-1&customfield_14=false&aggregate_16=&sequence_16=99&visibility_16=false&entitytypeid_16=-1&customfield_16=false&prop_summarize=false&SelectedFieldIds=&filter=&AdhocListPageNumber=1&AdhocListSortBy=&jsObjectStorage=report&filter=&ListPageNumber=1&ListSortBy=&jsObjectStorage=report"
    headers_RunReport_Productividad = {
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

    response_RunReport_Productividad = requests.request(
        "POST", HUN_URL_RUNREPORT, headers=headers_RunReport_Productividad, data=payload_RunReport_Productividad)
    # print(response_RunReport.text)
    # print(response_RunReport.text[2])

    response_dict_Productividad = json.loads(
        response_RunReport_Productividad.text)
    id_reporte_Productividad = str(response_dict_Productividad["LogId"])
    print("id_reporte_Productividad", id_reporte_Productividad)

    # Generar pestaña reporte

    payload_Html_Productividad = {}
    headers_Html_Productividad = {
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

    response_Html_Productividad = requests.request(
        "GET", HUN_URL_HTML + id_reporte_Productividad, headers=headers_Html_Productividad, data=payload_Html_Productividad)

    payload_Json_Productividad = "sort=&group=&filter="
    headers_Json_Productividad = {
        'authority': 'huntermonitoreopro.com',
        'accept': '*/*',
        'accept-language': 'en',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': l[1] + "; " + l[2] + "; " + CABECERA_ASPNET + l[0],
        'origin': HUN_URL_BASE,
        'referer': HUN_URL_HTML + id_reporte_Productividad,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    response_Json_Productividad = requests.request(
        "POST", HUN_URL_CAB_JSON + id_reporte_Productividad + HUN_URL_FIN_JSON, headers=headers_Json_Productividad, data=payload_Json_Productividad)
    # print(response_Json.text)
    data_dict_Productividad = json.loads(response_Json_Productividad.text)
    data_Productividad = data_dict_Productividad["Data"]
    for d in data_Productividad:
        lista_alias.append(d["Vehículo"])

        placa = convertir_placa(d["Vehículo"])
        lista_placa.append(placa)
        if d["TiempoRalentí"] == "":
            lista_ralenti.append(0)
        else:
            lista_ralenti.append(int(d["TiempoRalentí"])/3600)

        if d["Tiempodemanejo"] == "":
            lista_conduccion.append(0)
        else:
            lista_conduccion.append(int(d["Tiempodemanejo"])/3600)

        lista_distancia.append(d["Distanciatotal"])
        lista_velocidad_maxima.append(d["Velocidadmáxima"])

        porcentaje_ralenti = calcular_porcentaje_ralenti(
            d["TiempoRalentí"], d["Tiempodemanejo"])
        lista_porcentaje_ralenti.append(porcentaje_ralenti)

        if (d["Tiempodemanejo"] == "") or (d["Tiempodemanejo"] == "") or (d["Tiempodemanejo"] == "0"):
            dias_uso = 0
        else:
            dias_uso = 1
        lista_dias_uso.append(dias_uso)
        # lista_fecha.append(fecha_payload)
        # lista_proveedor.append("hunter_pro")

    dict_Productividad = {
        "placa": lista_placa,
        "descripcion_vehiculo": lista_alias,
        "distancia": lista_distancia,
        "horas_ralenti": lista_ralenti,
        "horas_movimiento": lista_conduccion,
        "velocidad_maxima": lista_velocidad_maxima,
        "dias_uso": lista_dias_uso,
    }
    # print(dict_Productividad)
    df_productividad = pd.DataFrame(dict_Productividad)
    df_productividad["fecha"] = fecha_payload[1]
    df_productividad["proveedor"] = "hunter_pro"
    return df_productividad
