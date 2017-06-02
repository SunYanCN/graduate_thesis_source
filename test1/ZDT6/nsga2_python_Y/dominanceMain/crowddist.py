#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
"""
拥挤距离计算
输入：
funScore=np.array([[1,2], [2,3], [2,2], [3,2], [4,3], [2,1], [3,1], [3,2], [3,3], [3,4]])

layerDict
{1: [4, 9], 2: [8], 3: [1, 3, 7], 4: [2, 6], 5: [0, 5]}
indicate 第五层 个体索引 [0, 5]
"""
def crowddist(funScore, indicate):
    #求出该层　评分子矩阵
    indicate=np.array(indicate)
    score=funScore[indicate] 

    #求出集合中 不同属性的 范围
    #rangeVector=np.array([1.0, 1.0])
    maxVector=np.max(funScore, axis=0)
    minVector=np.min(funScore, axis=0)
    rangeVector=(maxVector-minVector)*1.0

    #生成个体编号
    N=score.shape[0]
    V=score.shape[1]
    indicateVector=np.arange(N)
    indicateVectorT=indicateVector.reshape(N, 1)

    #生成 函数值和个体序号 矩阵
    dist=np.array([0.0]*N*V).reshape(N, V)
    scoreIndicateMatrix=np.hstack((score, indicateVectorT))

    scoreList=scoreIndicateMatrix.tolist()

    for i in xrange(V):
        scoreList.sort(key=lambda x:x[i])
        
        i_a=scoreList[0][-1]
        i_b=scoreList[-1][-1]
        dist[i_a][i]=1000000000000000
        dist[i_b][i]=1000000000000000

        for j in xrange(1, N-1):
            c=scoreList[j-1][i]
            d=scoreList[j+1][i]
            i_e=scoreList[j][-1]
            dist[i_e][i]=d-c

    distVector=np.sum(dist/rangeVector, axis=1) 
    
    dist_indicate=indicate[np.argsort(distVector)].tolist()

    return dist_indicate[::-1]


if __name__=="__main__":
    funScore=np.array([[1,2], [2,3], [2,2], [3,2], [4,3], [2,1], [3,1], [3,2], [3,3], [3,4]])
    layerDict={1: [4, 9], 2: [8], 3: [1, 3, 7], 4: [2, 6], 5: [0, 5]}

    print crowddist(funScore, layerDict[3])
   


