from math import pi

def circulo(raio): #Função
    return pi * raio ** 2

if __name__ == '__main__': #O padrão do módulo name é main
    raio = float(input('Informe o valor do raio: '))
    area = circulo(raio)
    print('Área do circulo', area)
