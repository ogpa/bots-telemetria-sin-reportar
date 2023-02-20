from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar


def fecha_hoy_hunter_pro():
    now = datetime.now()
    dia = str(now.day)
    mes = calendar.month_abbr[now.month]
    anho = str(now.year)

    fecha_fin_str = dia + "+" + mes + "+" + anho

    now = now - relativedelta(months=1)
    mes = calendar.month_abbr[now.month]
    fecha_inicio_str = dia + "+" + mes + "+" + anho
    # print(dia)
    # print(mes)
    # print(anho)
    # print(fecha_str)
    # print(fecha_inicio_str)
    # print(fecha_fin_str)

    return fecha_inicio_str, fecha_fin_str


# fecha_hoy_hunter_pro()
