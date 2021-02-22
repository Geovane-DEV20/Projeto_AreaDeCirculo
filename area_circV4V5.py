from math import pi

def circulo(raio):
    print('O valor do raio é', pi * raio ** 2)


if __name__ == '__main__': #O padrão do módulo name é main
    raio = float(input('Informe o valor do raio: '))
    circulo(raio)
