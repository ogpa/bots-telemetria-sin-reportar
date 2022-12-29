import time
import datetime
from email.utils import parsedate_to_datetime
fecha = "Thu, 29 Dec 2022 14:02:32 GMT"


def timestamp(dt):
    a = datetime.datetime.strptime(fecha, '%a, %d %b %Y %H:%M:%S GMT')
    print(a)

    epoch = datetime.datetime.utcfromtimestamp(0)
    m = round((a - epoch).total_seconds())

    print(m)


timestamp(fecha)
