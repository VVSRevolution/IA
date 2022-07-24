from random import *
from math import *
from typing import *

tamanhoPop = 100
tamanhoGen = 44
numGeracoes = 40
taxaMultacao = 0.8#%

Genoma = List[int]
class structPopulacao:
    def __init__(self,genoma,aptidao):
        self.genoma: Genoma = genoma
        self.aptidao: int = aptidao

Populacao = List[structPopulacao]
Aptidao = List[int]

def main():

    
    Populacao = gerarPopulacao(tamanhoPop,tamanhoGen)

    for i in range(tamanhoPop):
        print(f"{i}: {binToDec(Populacao[i].genoma[:22])} = {binToDec(Populacao[i].genoma[22:44])} f6: {f6(binToDec(Populacao[i].genoma[:22]),binToDec(Populacao[i].genoma[22:44]))}\n")
    
def gerarGenoma(largura: int) -> Genoma:
    return choices([0, 1],k=largura)

def gerarPopulacao(tamanhoPop: int, larguraGenoma: int):
    populacaoList = []
    for _ in range(tamanhoPop):
        populacaoList.append(structPopulacao(gerarGenoma(larguraGenoma),0))
    return populacaoList
    
def fitness(populacao:Populacao) -> Aptidao:
    pass

def f6(x,y):
    x = (x * 200/(2**22-1)) - 100                   
    y = (y * 200/(2**22-1)) - 100
    print(f"x={x} y={y}")
    return 0.5 - ((sin(sqrt(x**2+y**2)))**2 - 0.5)/(1 + 0.001*(x**2 + y**2))**2


def cruzamento(genoma1:Genoma, genoma2:Genoma):
    x = randint(1,43)
    temp1 = genoma1[:x] + genoma2[x:44]
    temp2 = genoma2[:x] + genoma1[x:44]
    genoma1 = temp1
    genoma2 - temp2

def multacao(genoma:Genoma):
    for i in range(tamanhoGen):
        if(random()*100<=taxaMultacao):
            if(genoma[i]==0): genoma[i]=1
            else: genoma[i]=0

def binToDec(genoma:Genoma) -> int:
    value = 0
    for i in range(tamanhoGen//2):
        digit = genoma.pop()
        if digit == 1:
            value = value + pow(2, i)
    return value

def roleta():
    pass


if __name__ == "__main__":
    main()
    