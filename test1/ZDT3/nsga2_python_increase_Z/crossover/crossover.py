#!/usr/bin/env python
#encoding:UTF-8 
import numpy as np
import random

"""
    SBX 交叉
"""
def crossover(population, alfa, i, tempDict, s):
    iDict=tempDict[0] 
    L=tempDict[1]
    T1=0.382*500
    T2=(1-0.382)*500
    T3=500
    if i<T1:
        a=0.25*(T1-i)/T1+0.75
    elif i<T2:
        a=0.25*(T2-i)/(T2-T1)+0.5
    else:
        a=(0.5*0.6)*(T3-i)/(T3-T2)+0.5*0.4

    eta_c=1.0+29.0*(i)/500#20.0
    alfa=a

    N=population.shape[0]
    V=population.shape[1]

    for i in xrange(0, N-1, 2):
        if s>0:
            b=min(iDict[i], iDict[i+1])
            if L!=1:
                alfa=alfa+(1.0-alfa)/(L-1)*(b-1)
                eta_c=eta_c-(eta_c-1.0)/(L-1)*(b-1)
            """
            elif s<300:
                alfa=(1.0+alfa)/2.0
                eta_c=(1.0+eta_c)/2.0
            else:
                alfa=1.0
                eta_c=1.0
            """
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




