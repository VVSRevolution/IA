
from operator import attrgetter
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

# fitness aptdao -> roleta -> cruzamento -> multacao -> deixar melhor pai

def main():
    populacaoFilho = []
    listCasais = List[int]
    Populacao = gerarPopulacao(tamanhoPop,tamanhoGen)
    fitness(Populacao)
    for j in range(numGeracoes):
        listCasais = roleta(Populacao)
        #print(f"list casais{listCasais}")
        for i in range(tamanhoPop//2):
            #print(f"cruzando {listCasais[i][0]} x {listCasais[i][1]}")
            tempGenoma = cruzamento(Populacao[listCasais[i][0]].genoma , Populacao[listCasais[i][1]].genoma)
            #print(f"resultados {tempGenoma[0]} x {tempGenoma[1]}")
            populacaoFilho.append(structPopulacao(tempGenoma[0],0))
            populacaoFilho.append(structPopulacao(tempGenoma[1],0))
        fitness(populacaoFilho)
        indexMax = Populacao.index(max(Populacao, key=attrgetter('aptidao')))
        #print(f"index {indexMax}")
        indexMin = populacaoFilho.index(min(populacaoFilho, key=attrgetter('aptidao')))
        #print(f"index {indexMin}")
        populacaoFilho[indexMin] = Populacao[indexMax]
        report =f"Melhor Genoma na [{indexMax}] geração ({j}): \t {getxyf6(Populacao[indexMax].genoma)}\nbinario: {Populacao[indexMax].genoma}"
        print(report)
        Populacao = 0
        Populacao = populacaoFilho
       


    #print(f"casais{listCasais}")

    #for i in range(tamanhoPop):
        #print(f"{i}: {binToDec(Populacao[i].genoma[:22])} = {binToDec(Populacao[i].genoma[22:44])} f6: {f6(binToDec(Populacao[i].genoma[:22]),binToDec(Populacao[i].genoma[22:44]))}\n")


def gerarGenoma(largura: int) -> Genoma:
    return choices([0, 1],k=largura)

def gerarPopulacao(tamanhoPop: int, larguraGenoma: int):
    populacaoList = []
    for _ in range(tamanhoPop):
        populacaoList.append(structPopulacao(gerarGenoma(larguraGenoma),0))
    return populacaoList
    
def fitness(populacao:Populacao) -> Aptidao:
    
    for i in range(tamanhoPop):
        populacao[i].aptidao = f6(binToDec(populacao[i].genoma[:22]),binToDec(populacao[i].genoma[22:44]))
            # print(populacao[i].aptidao)       

def f6(x,y) -> float:
    x = (x * 200/(2**22-1)) - 100                   
    y = (y * 200/(2**22-1)) - 100
    #print(f"x={x} y={y}")
    return 0.5 - ((sin(sqrt(x**2+y**2)))**2 - 0.5)/(1 + 0.001*(x**2 + y**2))**2

def cruzamento(genoma1:Genoma, genoma2:Genoma) -> Genoma:
    x = randint(1,43)
    temp1 = genoma1[:x] + genoma2[x:44]
    temp2 = genoma2[:x] + genoma1[x:44]
    genoma1 = temp1
    genoma2 = temp2

    return temp1, temp2

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

def roleta(populacao:Populacao):
    #populacao.sort(key=lambda x: x.aptidao)
    listposicao = []
    listpesos = []
    listcasais = []
    for i in range (tamanhoPop):
        listposicao.append(i)
        listpesos.append(populacao[i].aptidao)


    for i in range(tamanhoPop//2):
        result = choices(listposicao, weights = listpesos, k=2)
        listcasais.append(result)
    
    return listcasais

def getxyf6(genoma: Genoma):
    x = binToDec(genoma[:22])
    y = binToDec(genoma[22:44])
    f6r = f6(x,y)
    result = f"x = {x}\ty = {y}\tF6 = {f6r}"
    return result
    
if __name__ == "__main__":
    main()
