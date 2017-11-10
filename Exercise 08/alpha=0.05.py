# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:15:30 2017

@author: 高多奇
"""
import pylab as pl
import math 
import numpy as np   
x=0.1
y=0.1
t=0.
vx=1
vy=0.1
dt=0.001
time=0
X=[]
Y=[]
X1=[]
Y1=[]
while(t<100):
    x=x+vx*dt
    y=y+vy*dt
    vx=vx
    vy=vy
    t=t+dt
    if(x**2+(y+0.1)**2>1)and(y>0.1):
        P=np.array([x,y+0.1])
        n=P/math.sqrt(np.dot(P,P))
        V=np.array([vx,vy])
        v_1=np.dot(V,n)*n
        v_2=V-v_1
        v_1=-v_1
        [vx,vy]=v_1+v_2
        x=x+vx*dt
        y=y+vy*dt
    if(x**2+(y-0.1)**2>1)and(y<-0.1):
        P=np.array([x,y-0.1])
        n=P/math.sqrt(np.dot(P,P))
        V=np.array([vx,vy])
        v_1=np.dot(V,n)*n
        v_2=V-v_1
        v_1=-v_1
        [vx,vy]=v_1+v_2
        x=x+vx*dt
        y=y+vy*dt
    elif(abs(x)>0.95)and((x**2+(y+0.1)**2<1)or(x**2+(y-0.1)**2<1)):
        vx=-vx
        vy=vy
        x=x+vx*dt
        y=y+vy*dt
    X.append(x)
    Y.append(y)
    if(abs(y)<0.01):
        X1.append(x)
        Y1.append(vx)   
fig1=pl.figure(figsize=(10,5))
pl.subplot(121)
pl.title('stadium billiard trajectory alpha=0.05')
x=np.cos(np.linspace(0.1,np.pi,200))
y=np.sin(np.linspace(0,np.pi,200))-0.1
pl.plot(x,y,'r.')
x=np.cos(np.linspace(0.1,-np.pi,200))
y=np.sin(np.linspace(0,-np.pi,200))+0.1
pl.plot(x,y,'r.')    
pl.plot(X,Y,'b-')
pl.xlim(-1.2,1.2)
pl.ylim(-1.2,1.2)
pl.plot(x,y)
pl.ylabel('y')
pl.xlabel('x')
pl.subplot(122)
pl.title('stadium billiard phase space piot alpha=0.05')
pl.plot(X1,Y1,'.')
pl.xlim(-1.2,1.2)
pl.ylim(-1.2,1.2)
pl.ylabel('vx')
pl.xlabel('x')

pl.show()
