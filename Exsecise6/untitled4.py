# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:41:22 2017

@author: 高多奇
"""
import pylab as pl
import math   
g=9.8
l=9.8
dt=0.04
q=0.5
F=0.5
D=2.0/3.0
t=0
x=0.2
w=0
pi=math.pi
X=[0]
Y=[0]
while t<=5000:
    w=w-((g/l)*math.sin(x)+q*w-F*math.sin(D*t))*dt
    x=x+w*dt
    if x<=-1*pi:        
         x=x+2*pi
    elif x>=pi:
         x=x-2*pi
    else:
         x=x
    X.append(t)
    Y.append(x)  
    t=t+dt  
pl.plot(X, Y,'r-',label='w versus θ  F=0.5')
pl.title('')
pl.ylabel('θ(radians)')
pl.xlabel('time(s)')
pl.xlim(0, 60)
pl.ylim(-1.5,1.5)
pl.legend(loc = 'best')
