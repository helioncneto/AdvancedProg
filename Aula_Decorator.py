# -*- coding: utf-8 -*-

import datetime
def deco(func):
    def wrapper(*args, **kwargs):
        f = open('log.txt', 'a')
        f.write("A função " + func.__name__ + " foi executada em " + datetime.datetime.now().strftime("%d/%m/%Y") + "\n")
        resp = func(*args, **kwargs)
        f.write("A função " + func.__name__ + " foi finalizada e retornou " + str(resp))
        f.close()
        return resp
    return wrapper

@deco
def add(a, b):
    return a + b

if __name__ == '__main__':
    add(5, 10)