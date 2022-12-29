import time


def timestamp():
    t = time.time()
    t_ms = int(t * 1000)
    print(int(t//1))


timestamp()
