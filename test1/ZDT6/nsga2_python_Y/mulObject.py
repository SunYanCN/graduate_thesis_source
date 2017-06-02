#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
from function.funUserDefine import *
from selection.selection import selection
from crossover.crossover import crossover
from mutation.mutation import mutation
from dominanceMain.dominanceMain import dominanceMain
from dominanceMain.estimate import estimate
from dominanceMain.dynamic import dynamic 

#200个个体, 30个变量， 变量数值范围0到2**14
#交叉概率0.6， 编译概率0.1
xN=200
yN=10
alfa=0.8
belta=1.0/10

def run():
    s=0
    population=np.random.rand(xN, yN)
    functionObject=ZDT6(population)

    for i in xrange(500):
        f_population=population.copy()
        selection(population, functionObject)

        tempDict=dynamic(population, functionObject)
        crossover(population, alfa, i, tempDict, s)

        tempDict=dynamic(population, functionObject)
        mutation(population,  belta, i, tempDict, s)
        c_population=population

        temp_population=np.vstack((f_population, c_population))

        s=estimate(temp_population, functionObject).shape[0]
        print i, s

        population=dominanceMain(temp_population, functionObject)

    T0=estimate(population, functionObject).tolist()
    T1=set((k[0], k[1]) for k in T0)
    for k in T1:
        print k[0], k[1]

for i in xrange(100):
    print "Time", i
    run()

         
