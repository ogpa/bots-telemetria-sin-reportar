import time


def obtener_millis_now():
    t = time.time()
    t_ms = int(t//1)
    return str(t_ms)


# timestamp()
