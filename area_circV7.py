from math import pi
import sys

def circulo(raio): #Função
    return pi * float(raio) ** 2

if __name__ == '__main__': #O padrão do módulo name é main
    raio = sys.argv[]
    area = circulo(raio)
    print('Área do circulo', area)
