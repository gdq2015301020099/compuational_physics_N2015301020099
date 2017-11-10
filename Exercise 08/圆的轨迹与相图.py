# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:33:24 2017

@author: 高多奇
"""

import pylab as pl
import math 
import numpy as np   
x=0.5
y=0.5
t=0.
vx=0.71
vy=0.51
dt=0.01
time=0
X=[]
Y=[]
X1=[]
Y1=[]
while(t<300):
    x=x+vx*dt
    y=y+vy*dt
    vx=vx
    vy=vy
    t=t+dt
    if(x**2+y**2>1):
        P=np.array([x,y])
        n=P/math.sqrt(np.dot(P,P))
        V=np.array([vx,vy])
        v_1=np.dot(V,n)*n
        v_2=V-v_1
        v_1=-v_1
        [vx,vy]=v_1+v_2
        x=x+vx*dt
        y=y+vy*dt
    
    X.append(x)
    Y.append(y)
    if(abs(y)<0.001):
        X1.append(x)
        Y1.append(vx)
x=np.cos(np.linspace(0,2*np.pi,200))
y=np.sin(np.linspace(0,2*np.pi,200))        
fig1=pl.figure(figsize=(12,5))
pl.subplot(121)
pl.title('Circular stadium-trajectory')
pl.plot(X,Y,'')
pl.xlim(-1.2,1.2)
pl.ylim(-1.2,1.2)
pl.plot(x,y)
pl.ylabel('y')
pl.xlabel('x')
pl.subplot(122)
pl.title('Circular stadium-phase space piot')
pl.plot(X1,Y1,'.')
pl.xlim(-1.2,1.2)
pl.ylim(-1.2,1.2)
pl.ylabel('vx')
pl.xlabel('x')

pl.show()
