#!/usr/bin/env python
#encoding:UTF-8 
import numpy as np
import random

"""
    SBX 交叉
"""
def crossover(population, alfa):
    eta_c=20.0

    N=population.shape[0]
    V=population.shape[1]

    for i in xrange(0, N-1, 2):
        if random.random()>alfa:
            continue

        #对两个个体执行SBX交叉操作 
        for j in xrange(V):
            #对某自变量交叉
            ylow=0.0 #
            yup=1.0 #
            y1=population[i][j]
            y2=population[i+1][j]
            r=random.random()
            if r<=0.5:
                betaq=(2*r)**(1.0/(eta_c+1.0))
            else:
                betaq=(0.5/(1.0-r))**(1.0/(eta_c+1.0))

            child1=0.5*( (1+betaq)*y1+(1-betaq)*y2 )
            child2=0.5*( (1-betaq)*y1+(1+betaq)*y2 )
            child1=min(max(child1, ylow), yup)
            child2=min(max(child2, ylow), yup)

            population[i][j]=child1
            population[i+1][j]=child2


###以下是测试用例
if __name__=="__main__":
    np.random.seed(0)
    xN=5
    yN=3
    alfa=0.6
    population=np.random.rand(xN, yN)

    print population
    ###运行函数
    crossover(population, alfa)
    print population




