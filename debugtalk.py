import time


def sleep(n_secs):
    time.sleep(n_secs)


def get_timestamp():
    return str(int(time.time() * 10))


# 11位
def get_timestamp2():
    return str(int(time.time() * 10))


# 5位
def name_timestamp():
    return str(time.time()).replace(".", "")[6:10]
