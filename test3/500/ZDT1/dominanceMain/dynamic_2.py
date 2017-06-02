#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
from dominance import dominance
from rank import rank

def dynamic_2(population, functionObject):
    ###为函数对象赋值新的种群个体
    functionObject.population=population

    #计算新种群目标函数数值，并建立矩阵 funScore
    funScore=np.vstack((functionObject.objFun_1(), functionObject.objFun_2()))
    funScore=np.transpose(funScore)

    #输入函数数值矩阵，求得个体 分层和拥挤距离 字典
    r_dict=dominance(funScore)
    layerDict=rank(r_dict)
   
    valueDict={}
    funScoreList=funScore.tolist()
    for k in xrange(population.shape[0]):
        valueDict[k]=(funScoreList[k][0], funScoreList[k][1])
     
    iDict={}
    for k, v in layerDict.items():
        for w in v:
            iDict[w]=k
    
    return layerDict, valueDict, iDict




if __name__=="__main__":
    np.random.seed(0)
    random.seed(0)
    from function.funUserDefine import *
    population=np.random.rand(10, 3)
    functionObject=ZDT1(population)

    print dominanceMain(population, functionObject)



