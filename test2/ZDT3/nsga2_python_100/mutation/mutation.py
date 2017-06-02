#!/usr/bin/env python
#encoding:UTF-8 
import numpy as np
import random

def mutation(population, belta):
    eta_m=20.0

    N=population.shape[0]
    V=population.shape[1]

    for i in xrange(N):
        for j in xrange(V):
            r=random.random()
            #对个体某变量进行变异
            if r<=belta:
                y=population[i][j]
                ylow=0.0
                yup=1.0
                delta1=1.0*(y-ylow)/(yup-ylow)
                delta2=1.0*(yup-y)/(yup-ylow)
                
                r=random.random()
                mut_pow=1.0/(eta_m+1.0)
                if r<=0.5:
                    xy=1.0-delta1
                    val=2.0*r+(1.0-2.0*r)*(xy**(eta_m+1.0))
                    deltaq=val**mut_pow-1.0
                else:
                    xy=1.0-delta2
                    val=2.0*(1.0-r)+2.0*(r-0.5)*(xy**(eta_m+1.0))
                    deltaq=1.0-val**mut_pow
                y=y+deltaq*(yup-ylow)
                y=min(yup, max(y, ylow))
                population[i][j]=y


###以下是测试用例
if __name__=="__main__":
    np.random.seed(0)
    xN=5
    yN=3
    belta=0.3
    population=np.random.rand(xN, yN)

    print population
    ###运行函数
    mutation(population, belta)
    print population

