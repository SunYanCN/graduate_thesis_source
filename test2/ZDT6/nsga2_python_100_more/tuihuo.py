#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
from dominanceMain.dynamic_2 import dynamic_2
from math import exp

def inner(k, population, layerDict, valueDict, iDict, Tk, p_list, functionObject):
    Kt=500.0#自设置
    N=len(iDict)
    iRank=iDict[k]
    individual=population[k,:].copy()

    individual+=(2*np.random.random(10)-1.0)*Tk/3000.0#
    individual[individual>1.0]=1.0#
    individual[individual<0.0]=0.0#

    functionObject.population=individual.reshape(1,10)
    funScore=np.vstack((functionObject.objFun_1(),functionObject.objFun_2()))
    funScore=np.transpose(funScore).tolist()[0]

    j=valueDict[k]
    i=k
    if((j[0]>funScore[0]) and (j[1]==funScore[1])):
            population[i,:]=individual
            valueDict[i]=funScore 
            return True
    elif((j[0]==funScore[0]) and (j[1]>funScore[1])):
            population[i,:]=individual
            valueDict[i]=funScore
            return True
    elif((j[0]>funScore[0]) and (j[1]>funScore[1])):
            population[i,:]=individual
            valueDict[i]=funScore
            return True
    return False

    """
    m=0
    flage=False
    for w in xrange(len(layerDict[1])):
        i=layerDict[1][w]
        j=valueDict[i]
        if((j[0]<funScore[0]) and (j[1]==funScore[1])):
            m+=1
        elif((j[0]==funScore[0]) and (j[1]<funScore[1])):
            m+=1
        elif((j[0]<funScore[0]) and (j[1]<funScore[1])):
            m+=1
               
        if((j[0]>funScore[0]) and (j[1]==funScore[1])):
            population[i,:]=individual
            flage=True
            valueDict[i]=funScore 
            #print "*"*100
        elif((j[0]==funScore[0]) and (j[1]>funScore[1])):
            population[i,:]=individual
            flage=True
            valueDict[i]=funScore
            #print "*"*100
        elif((j[0]>funScore[0]) and (j[1]>funScore[1])):
            population[i,:]=individual
            flage=True
            valueDict[i]=funScore
            #print "*"*100
        
        if((j[0]==funScore[0]) and (j[1]==funScore[1])):
            return False  

    if m==0:
        if(not flage):
            iDict[N]=1
            p_list.append(individual)
        return True
    else:
        r=random.random() 
        t=exp(-Kt/Tk*m/200.0)#len(layerDict[1]))
        if r<=t:
            iDict[N]=1
            p_list.append(individual)
            return True
    
    return False
    """
def tuihuo(population, functionObject, times):
    Tk=1000*(0.95**times)    
    layerDict, valueDict, iDict=dynamic_2(population, functionObject)
    p_list=[]

    for k in xrange(population.shape[0]):
    #for k in layerDict[1]:
        w=0
        flage=False
        #while(w<5 and (not flage)):
        while(w<5):
            flage=inner(k, population, layerDict, valueDict, iDict, Tk, p_list, functionObject)
            w+=1
    return p_list, iDict  
