from math import pi
import sys
import errno

def help():
    print("É necessario informar o raio do círculo.")
    print("Sintaxe: {}  <raio> ".format(sys.argv[0][2:]))

def circulo(raio): #Função
    return pi * float(raio) ** 2

if __name__ == '__main__': #O padrão do módulo name é main'
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM) #Sys.exit retornou com erro

    # else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do circulo', area)

