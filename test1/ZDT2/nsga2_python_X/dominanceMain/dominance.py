#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
"""
        支配关系字典 r_dict
        建立 {个体号码：[支配其的个数， 被其支配的个体列表]}
"""
def dominance(funScore):
    #支配关系字典
    r_dict={}

    #需要建立支配关系的 个体数
    N=funScore.shape[0]

    #建立个体索引 向量
    indicateVector=np.arange(N)
    
    #建立 元素全为1 的 列向量 
    oneVector=np.array([1]*N).reshape(N, 1)
    
    for k in xrange(N): 
        #建立 行向量全为 第k个个体评分的 矩阵
        oneMatrix=oneVector*funScore[k, ]
        
        #建立支配关系判断的 差分矩阵
        diffMatrix=funScore-oneMatrix
   
        greaterMatrix=(diffMatrix>=0)
        lessMatrix=(diffMatrix<=0)
        equalMatrix=(diffMatrix==0)

        greaterVector=np.all(greaterMatrix, axis=1)
        lessVector=np.all(lessMatrix, axis=1)
        equalVector=np.all(equalMatrix, axis=1)
            
        #建立非支配、支配向量
        dominate=indicateVector[greaterVector-equalVector, ]
        nonDominate=indicateVector[lessVector-equalVector, ]
        
        #建立支配关系字典
        r_dict[k]=[len(nonDominate), list(dominate)]

    return r_dict


if __name__=="__main__":
    funScore=np.array([[1,2], [2,3], [2,2], [3,2], [4,3], [2,1], [3,1], [3,2], [3,3], [3,4]])
    print dominance(funScore)
    
