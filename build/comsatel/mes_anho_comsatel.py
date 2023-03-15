from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale

#diafijo = datetime(2023, 1, 15)


def mes_anho_comsatel():
    locale.setlocale(locale.LC_ALL, 'es_ES')
    last_day = datetime.now() - relativedelta(days=1)

    mes = format(last_day, '%B').upper()
    anho = format(last_day, '%Y')

    # print(mes)
    # print(anho)

    return mes, anho
