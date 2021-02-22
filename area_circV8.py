from math import pi
import sys

def circulo(raio): #Função
    return pi * float(raio) ** 2

if __name__ == '__main__': #O padrão do módulo name é main'
    if len(sys.argv) < 2:
        print("É necessario informar o raio do círculo.")
        print("Sintaxe: {}  <raio> ".format(sys.argv[0][44:55]))
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do circulo', area)

