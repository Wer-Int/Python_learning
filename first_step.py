from math import *
a,b,c = eval(input())
if a!=0:
    d=b*b-4*a*c
    if d<0: print(0)
    elif d==0:
        if (t:=-b/(2*a))>0: print(-sqrt(t),sqrt(t))
        elif b==0: print(0.0)
        else: print(0)
    else:
        t1=(-b+sqrt(d))/(2*a)
        t2=(-b-sqrt(d))/(2*a)
        if t1>0 and t2>0: 
            if abs(t1)>abs(t2): print(-sqrt(t1),-sqrt(t2),sqrt(t2),sqrt(t1))
            else: print(-sqrt(t2),-sqrt(t1),sqrt(t1),sqrt(t2))
        elif t1>0: 
            if t2==0: print(-sqrt(t1),0,sqrt(t1))
            else: print(-sqrt(t1),sqrt(t1))
        elif t2>0: 
            if t1==0: print(-sqrt(t2),0,sqrt(t2))
            else: print(-sqrt(t2),sqrt(t2))
        else: print(0)
elif b!=0: 
    if -c/b>0: print(-sqrt(-c/b),sqrt(-c/b))
    elif c==0: print(0.0)
    else: print(0)
elif c!=0: print(0)
else: print(-1)