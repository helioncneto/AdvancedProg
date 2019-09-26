# -*- coding: utf-8 -*-

def dec_factory(a):
    if isinstance(a, str):
        def str_decorator(func):
            def str_wrapper():
                print("A variável é uma String")
                func(a)
            return str_wrapper
        return str_decorator
    elif isinstance(a, int):
        def int_decorator(func):
            def int_wrapper():
                print("A variável é um Inteiro")
                func(a)
            return int_wrapper
        return int_decorator
    else:
        def badtype_decorator(func):
            def badtype_wrapper():
                print("Bad Type")
                func(a)
            return badtype_wrapper
        return badtype_decorator

@dec_factory("Helio")
def seu_nome(nome):
    print("Seu nome é %s" % nome)

@dec_factory(29)
def sua_idade(idade):
    print("Sua idade é %d" % idade)

@dec_factory(75.5)
def seu_peso(peso):
    print("Seu peso é %d" % peso)

if __name__ == '__main__':
    seu_nome()
    sua_idade()
    seu_peso()


