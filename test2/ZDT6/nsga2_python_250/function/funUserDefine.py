#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
from funModel import *
### 以下为具体实现函数
### 需要用户自定义函数，继承与上面的模板抽象函数
#######################################################
class ZDT6(objectFun_2):
    #ZDT6函数
    def gFun(self):
        N=self.population.shape[1]-1
        return 1+9.0*(( np.sum(self.population[:,1:], axis=1)/N )**0.25)

    def objFun_1(self):
        return 1.0-np.exp(-4.0*self.population[:,0])*( np.sin(6.0*np.math.pi*self.population[:,0])**6.0 )

    def objFun_2(self):
        temp=1-np.square(self.objFun_1()/self.gFun())
        return self.gFun()*temp

#######################################################


###测试函数  如下
if __name__=="__main__":
    np.random.seed(0)
    zdt6=ZDT6(np.random.rand(20, 3))
    print zdt6.objFun_1()
    print zdt6.objFun_2()



