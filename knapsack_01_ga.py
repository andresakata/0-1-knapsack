from execution_logger import ExecutionLogger
from dataset_reader import DatasetReader
import random
from operator import itemgetter

# Static position
nNUM_GENERATION = 1000
nNUM_TEST = 100

class KnapsackGeneticAlgorithm:
  def __init__(self, n, weight, profit, max_weight):
    self.n = n
    self.weight = weight
    self.profit = profit
    self.max_weight = max_weight

  def run(self):
    self.best_value = 0
    self.total_weight = 0
    self.s = []
    self.solve(self.n, self.s, 0, 0)

  def solve(self, n, s, current_w, current_v):

    nTest = 0

    while nTest <= nNUM_TEST:
        nCnt = 0
        #Determina os valores dos primeiros individuos
        aGroupIndividual = [self.aleatory_population(n),self.aleatory_population(n),self.aleatory_population(n)]
        #print(aGroupIndividual)
        #Determina quantas gerações irá executar
        while nCnt <= nNUM_GENERATION:
            aBestIndividual = self.fitness(aGroupIndividual)
            aGroupIndividual = self.crossover(aBestIndividual)
            nCnt += 1

        # Executa um último fitness para avaliar os melhores individuos
        aOrderIndividual = self.fitness(aGroupIndividual, True)
        if len(aOrderIndividual) > 0:
            cBestIndividual = aOrderIndividual[0]
            aValuete = self.evaluete_individual(cBestIndividual)
            if self.best_value < aValuete[1]:
                self.best_value = aValuete[1]
                self.total_weight = aValuete[0]
                self.s = []
                for cChromo in cBestIndividual:
                    self.s.append(int(cChromo))
        nTest += 1

  def aleatory_population(self, nNumitens):

    cReturn = ""
    for nCnt in range(nNumitens):
        nRandom = random.randint(0,1)
        cReturn = cReturn + str(nRandom)

    return cReturn
  def evaluete_individual(self, cIndividual):

    nWeight = 0
    nValue = 0
    nCnt = 0
    for cPos in cIndividual:
        if cPos == "1":
            nWeight = nWeight + self.weight[nCnt]
            nValue = nValue + self.profit[nCnt]
        nCnt += 1

    if nWeight == 0:
        nRatio = 0
    else:
        nRatio = nValue/nWeight

    return [nWeight, nValue, nRatio ]

  def fitness(self, aGroupIndividual, lLast = False):

    aEvalueteIndividual = []
    aNewIndividual = []

    for cIndividual in aGroupIndividual:
        aTmp = self.evaluete_individual(cIndividual)
        aEvalueteIndividual.append([cIndividual, aTmp[0], aTmp[1], aTmp[2]])

    # Ordena os elementos pelo valor
    aEvalueteIndividual = sorted(aEvalueteIndividual, key=itemgetter(2), reverse=True)

    # Busca os melhores elementos verificando o peso
    for aIndividual in aEvalueteIndividual:
        if aIndividual[1] <= self.max_weight:
            aNewIndividual.append(aIndividual[0])
        if len(aNewIndividual) == 2:
            break

    # Caso não tenha encontrado, adiciona os primeiros
    if not lLast and len(aNewIndividual) < 2:
        for aIndividual in aEvalueteIndividual:
            aNewIndividual.append(aIndividual[0])
            if len(aNewIndividual) == 2:
                break

    return aNewIndividual

  def crossover( self, aBestIndividual ):

    aNewPopulation = []

    cFather1 = aBestIndividual[0]
    cFather2 = aBestIndividual[1]

    # Define um cromossomo aleatório de fixação
    nFixChromo = int(self.n * random.random())

    # Fixa os cromossomos pais
    cChromoF1 = cFather1[:nFixChromo]
    cChromoF2 = cFather2[:nFixChromo]

    # Salva os cromossomos para descendência
    cChromo2F1 = cFather1[nFixChromo:]
    cChromo2F2 = cFather2[nFixChromo:]

    # Define os novos individuos
    aNewPopulation.append(cChromoF1 + cChromo2F2)
    aNewPopulation.append(cChromoF2 + cChromo2F1)

    # Aplica a mutação sobre um dos individuos aleatórios

    # Seleciona o individuo aleatorio
    nMutantIndividual = random.randint(0,1)
    cMutantIndividual = aNewPopulation[nMutantIndividual]

    # Troca simples de Cromossomos
    # Aplica a troca de gene aleatoriamente no Cromossomo Pai
    nRandomChange = nFixChromo
    while nRandomChange > len(cMutantIndividual)-1:
        nRandomChange = random.randint(1,nFixChromo)

    aMutantIndividual = list(cMutantIndividual)
    if cMutantIndividual[nRandomChange] == "0":
        aMutantIndividual[nRandomChange] = "1"
    else:
        aMutantIndividual[nRandomChange] = "0"
    cNewIndividual = "".join(aMutantIndividual)

    # Aplica a troca de gene aleatoriamente no Cromossomo Filho
    nRandomChange = self.n
    while nRandomChange > len(cMutantIndividual)-1:
        nRandomChange = random.randint(nFixChromo,self.n)

    aMutantIndividual = list(cNewIndividual)
    if cMutantIndividual[nRandomChange] == "0":
        aMutantIndividual[nRandomChange] = "1"
    else:
        aMutantIndividual[nRandomChange] = "0"
    cNewIndividual = "".join(aMutantIndividual)

    '''
    # Troca aleatório de Cromossomos
    cNewIndividual = ""
    for cChromo in cMutantIndividual:
        nRandomChange = random.randint(0,1)
        # Se for multiplo de 2 (par) troca
        if nRandomChange == 1:
            if cChromo == "1":
                cNewIndividual += "0"
            else:
                cNewIndividual += "1"
        else:
            cNewIndividual += cChromo
    '''
    aNewPopulation.append(cNewIndividual)

    # Adiciona os pais na nova população
    aNewPopulation.append(cFather1)
    aNewPopulation.append(cFather2)

    return aNewPopulation

dataset = DatasetReader().read('p08')
kbf = KnapsackGeneticAlgorithm(len(dataset[0]), dataset[0], dataset[1], dataset[2])
ExecutionLogger().run(kbf)