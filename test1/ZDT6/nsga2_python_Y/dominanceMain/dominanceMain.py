#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
from dominance import dominance
from rank import rank
from crowddist import crowddist

def dominanceMain(population, functionObject):
    ###为函数对象赋值新的种群个体
    functionObject.population=population

    #计算新种群目标函数数值，并建立矩阵 funScore
    funScore=np.vstack((functionObject.objFun_1(), functionObject.objFun_2()))
    funScore=np.transpose(funScore)

    N=population.shape[0]
    nN=N/2

    #输入函数数值矩阵，求得个体 分层和拥挤距离 字典
    r_dict=dominance(funScore)
    layerDict=rank(r_dict)

    s=0
    indicate=[]
    for i in xrange(1, len(layerDict)+1):
        s+=len(layerDict[i])  
        if s<nN:
            indicate.extend(layerDict[i])
            continue
        elif s==nN:
            indicate.extend(layerDict[i])
            break
        else:
            s-=len(layerDict[i])
            temp=crowddist(funScore, layerDict[i])
            indicate.extend(temp[:nN-s])
            break
            
    #返回新种群
    return population[indicate] 


if __name__=="__main__":
    np.random.seed(0)
    random.seed(0)
    from function.funUserDefine import *
    population=np.random.rand(10, 3)
    functionObject=ZDT1(population)

    print dominanceMain(population, functionObject)



