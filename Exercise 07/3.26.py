# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:41:22 2017

@author: 高多奇
"""
import pylab as pl
import math   
pl.figure(figsize=(12,7)) 

r=[25]
for i in range(len(r)):
    sigma=10
    b=8.0/3.0
    dt=0.0001
    x=1.
    y=0.
    z=0.
    t=0.
    X=[0]
    Y=[0]
    while(t<=50):
        a_x=sigma*(y-x)
        a_y=-x*z+r[i]*x-y
        a_z=x*y-b*z
        x=x+a_x*dt
        y=y+a_y*dt
        z=z+a_z*dt
        t=t+dt
        X.append(z)
        Y.append(y)
    pl.plot(X, Y,'r-',label='y versus z r='+str(r[i]))
    pl.title('z versus y')
    pl.ylabel('y')
    pl.xlabel('z')
    pl.xlim(0,25)
    pl.ylim(-15,15)
    pl.legend(loc = 'best')


    
