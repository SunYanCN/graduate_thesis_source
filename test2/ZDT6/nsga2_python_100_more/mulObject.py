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
from dominanceMain.dynamic_2 import dynamic_2
from math import exp
from tuihuo import tuihuo

#200个个体, 10个变量
#交叉概率0.6， 编译概率0.1
xN=200
yN=10
alfa=0.8
belta=1.0/10

def run():
    population=np.random.rand(xN, yN)
    functionObject=ZDT6(population)

    for i in xrange(100):
        if i>=0:     
            p_list, iDict=tuihuo(population, functionObject, i)
            for x in p_list:
                population=np.vstack((population, x))

        f_population=population.copy()
        selection(population, functionObject)
        crossover(population, alfa)
        mutation(population,  belta)

        if i>=0:     
            p_list, iDict=tuihuo(population, functionObject, i)
            for x in p_list:
                population=np.vstack((population, x))

        c_population=population

        temp_population=np.vstack((f_population, c_population))
        T0=estimate(temp_population, functionObject).tolist()
        T1=set((k[0], k[1]) for k in T0)
        print i, len(T1)

        population=dominanceMain(temp_population, functionObject)

    T0=estimate(population, functionObject).tolist()
    T1=set((k[0], k[1]) for k in T0)
    for k in T1:
        print k[0], k[1]

for i in xrange(100):
    print "Time", i
    run()

