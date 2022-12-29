import datetime

# fecha en formato "Thu, 29 Dec 2022 14:02:32 GMT"


def obtener_millis(fecha):
    a = datetime.datetime.strptime(fecha, '%a, %d %b %Y %H:%M:%S GMT')
    epoch = datetime.datetime.utcfromtimestamp(0)
    m = round((a - epoch).total_seconds())

    return str(m)


# timestamp(fecha)
