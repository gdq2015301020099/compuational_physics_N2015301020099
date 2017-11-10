# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 10:20:32 2017

@author: 高多奇
"""

import pylab as pl
import math 
import numpy as np   
x=-math.sqrt(3)
y=0.
t=0.
vx=1
vy=1
dt=0.01
time=0
X=[]
Y=[]
X1=[]
Y1=[]
while(t<800):
    x=x+vx*dt
    y=y+vy*dt
    vx=vx
    vy=vy
    t=t+dt
    if((x**2)/4+y**2>1):
        P=np.array([x/4,y])
        n=P/math.sqrt(np.dot(P,P))
        V=np.array([vx,vy])
        v_1=np.dot(V,n)*n
        v_2=V-v_1
        v_1=-v_1
        [vx,vy]=v_1+v_2
        x=x+vx*dt
        y=y+vy*dt
    elif(abs(x)>1.9)and(x**2/4+y**2<1):
        vx=-vx
        vy=vy
        x=x+vx*dt
        y=y+vy*dt
    X.append(x)
    Y.append(y)
    if(abs(y)<0.001):
        X1.append(x)
        Y1.append(vx)
x=2*np.cos(np.linspace(0,2*np.pi,200))
y=np.sin(np.linspace(0,2*np.pi,200))        
fig1=pl.figure(figsize=(12,5))
pl.subplot(121)
pl.title('a=2,b=1,trajectory')
pl.plot(X,Y,'')
pl.xlim(-2,2)
pl.ylim(-2,2)
pl.plot(x,y)
pl.ylabel('y')
pl.xlabel('x')
pl.subplot(122)
pl.title('a=2,b=1,phase space piot')
pl.plot(X1,Y1,'.')
pl.xlim(-2,2)
pl.ylim(-3,3)
pl.ylabel('vx')
pl.xlabel('x')

pl.show()
