from multiprocessing.pool import RUN
from random import *
from math import *

#BACH [0]
#BEETHOVEN [1]
#EINSTEIN [2]
#KEPLER [3]
TaxaAprendizado = 1
N1 = [0,0,1,1]
N2 = [0,1,0,1]
Saida = [0,0,1,1]
Pesos = [0,0,0]
Bias = 1
Wb = 0


def main():

    RUN = True
    while RUN:
        STOP = 0
        for i in range(4):
            if(calcularSaida(i)>0):
                sinaldeSaida = 1
            else: sinaldeSaida = calcularSaida(i)

            if (sinaldeSaida != Saida[i]):
                STOP = 1
                ajustarPeso(Saida[i] - calcularSaida(i),i)
            print(Pesos)    
    print(Pesos)
            


def calcularSaida(Posiçao):
    return (Bias + Pesos[0])+(N1[Posiçao]*Pesos[1])+(N1[Posiçao]*Pesos[2])

def ajustarPeso(valorErro, Posicao):
    Pesos[0] = Pesos[0] + (valorErro * TaxaAprendizado * Bias)
    Pesos[1] = Pesos[1] + (valorErro * TaxaAprendizado * N1[Posicao])
    Pesos[2] = Pesos[2] + (valorErro * TaxaAprendizado * N2[Posicao])

if __name__ == "__main__":
    main()
