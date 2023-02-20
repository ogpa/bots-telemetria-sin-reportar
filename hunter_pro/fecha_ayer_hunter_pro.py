from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar


def fecha_ayer_hunter_pro():
    now = datetime.now()
    ayer = now - relativedelta(days=1)
    dia = str(ayer.day)
    mes = calendar.month_abbr[ayer.month]
    anho = str(ayer.year)

    ayer_str = dia + "+" + mes + "+" + anho
    # print(ayer_str)

    return ayer_str


# fecha_ayer_hunter_pro()
