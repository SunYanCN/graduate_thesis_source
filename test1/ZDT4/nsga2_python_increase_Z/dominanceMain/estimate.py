#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
from dominance import dominance
from rank import rank

def estimate(population, functionObject):
    ###为函数对象赋值新的种群个体
    functionObject.population=population

    #计算新种群目标函数数值，并建立矩阵 funScore
    funScore=np.vstack((functionObject.objFun_1(), functionObject.objFun_2()))
    funScore=np.transpose(funScore)

    #输入函数数值矩阵，求得个体 分层和拥挤距离 字典
    r_dict=dominance(funScore)
    layerDict=rank(r_dict)

    return funScore[layerDict[1]]





if __name__=="__main__":
    np.random.seed(0)
    random.seed(0)
    from function.funUserDefine import *
    population=np.random.rand(10, 3)
    functionObject=ZDT1(population)

    print dominanceMain(population, functionObject)



