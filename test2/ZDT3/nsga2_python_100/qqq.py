import numpy as np

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
        temp=s_1[Time_list[k]+1+100:Time_list[k+1]]
        sss_1.append(temp)
    temp=s_1[Time_list[-1]+1+100:]
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
    f=open('paretoZDT3.dat')
    s_2=f.readlines()
    f.close()

    sss_2=[]
    for k in s_2:
        a,b=k.split()
        a=float(a.strip())
        b=float(b.strip())
        sss_2.append((a, b))
    return sss_2






def inner(x, y):
    df=((x[0][0]-y[0][0])**2+(x[0][1]-y[0][1])**2)**0.5
    dl=((x[-1][0]-y[-1][0])**2+(x[-1][1]-y[-1][1])**2)**0.5

    di=[]
    for i in xrange(1, len(x)):
        temp=((x[i-1][0]-x[i][0])**2+(x[i-1][1]-x[i][1])**2)**0.5
        di.append(temp)

    di=np.mean(di)

    dba=di.mean()

    d_abs=np.abs(di-dba)

    score=( df+dl+np.sum(d_abs) )/( df+dl+ (len(x)-1)*dba )

    return score


def fun():
    sss_b=fun_2()
    sss_b.sort()

    list_s=[]
    sss=fun_1()
    for sss_a in sss:##########################################
        sss_a.sort()
        list_s.append( inner(sss_a, sss_b) )

    s=np.array(list_s)
    print s
    print np.mean(s)
    print np.std(s)
fun()
