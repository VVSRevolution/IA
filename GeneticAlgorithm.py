from random import *
from math import *
from typing import List

tamanhoPop=100
tamanhoGen = 44
numGeracoes = 40
taxaMultacao = 0.8#%

Genoma = List[int]
Populacao = List[Genoma]

def main():
    
    Populacao = gerarPopulacao(tamanhoPop,tamanhoGen)
    print(f"meu: {f6(10,10)}\n gabriel: {f6g(10,10)}")

    
def gerarGenoma(largura: int) -> Genoma:
    return choices([0, 1],k=largura)

def gerarPopulacao(tamanhoPop: int, larguraGenoma: int) -> Populacao:
    return[gerarGenoma(larguraGenoma)for _ in range(tamanhoPop)]

def fitness(genome:Genoma, limitePeso: int) -> int:
    pass

def f6(x,y):    #função a ser maximizada
    return 0.5 - ((sin(sqrt(x**2+y**2)))**2 - 0.5)/(1 + 0.001*(x**2 + y**2))**2

def multacao(genoma:Genoma):
    for i in range(tamanhoGen):
        if(random()*100<=taxaMultacao):
            if(genoma[i]==0): genoma[i]=1
            else: genoma[i]=0

def binToDec(genoma:Genoma) -> int:
    value = 0
    for i in range(tamanhoGen):
        digit = genoma.pop()
        if digit == '1':
            value = value + pow(2, i)
    return value


if __name__ == "__main__":
    main()
    