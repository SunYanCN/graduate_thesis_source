def fun_1():
    f=open('1.txt')
    s_1=f.readlines()
    f.close()

    Time_list=[]
    for k in xrange(len(s_1)):
        if "Time" in s_1[k]:
            Time_list.append(k)

    sss_1=[]
    for k in xrange(len(Time_list)-1):
        temp=s_1[Time_list[k]+1+500:Time_list[k+1]]
        sss_1.append(temp)
    temp=s_1[Time_list[-1]+1+500:]
    sss_1.append(temp)

    sss_11=[]
    for k in sss_1:
        temp=[]
        for v in k:
            a,b=v.split()
            a=float(a.strip())
            b=float(b.strip())
            temp.append((a, b))
        sss_11.append(temp)
    return sss_11

def fun_2():
    f=open('paretoZDT6.dat')
    s_2=f.readlines()
    f.close()

    sss_2=[]
    for k in s_2:
        a,b=k.split()
        a=float(a.strip())
        b=float(b.strip())
        sss_2.append((a, b))
    return sss_2

def fun():
    sss1=fun_1()
    sss2=fun_2()

    result=[]
    for w in sss1:
        score=[]
        for k in w:
            p=[]
            for v in sss2:
                p.append( ((k[0]-v[0])**2+(k[1]-v[1])**2)**0.5 )
            score.append( min(p) )
        result.append(sum(score)/len(score))
    return result

import numpy as np
x=np.array(fun())
print len(x)
print np.mean(x)
print np.std(x)


