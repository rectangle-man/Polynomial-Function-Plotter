import numpy as np
from matplotlib import pyplot as plt
import random


def polyplot(x,cof):
  
  x=x.split(",")
  cof=cof.split(",")

  x=list(map(int,x))
  cof=list(map(int,cof))

  greet=['Hold up','Hang in there','Kindly wait','Hol\'up a min','Please wait','Pls wait']

  print(f"{random.choice(greet)}, your graph is being processed.")
  

  

  def pplot(x,cofe):
    c = len(cofe)
    y = 0
    for i in range(c):
        y += cof[i]*(x**i)
    return y

  x1 = np.linspace(x[0],x[1],x[2])
  f1=pplot(x1,cof)

  def fname(cof):
    t=''
    for i in range(len(cof)):
        c=str(cof[i])
        ex="x^"
        pow=str(i)
        s=c+ex+pow
        t+=s
        t+=" "
        if i!= len(cof)-1:
            t+='+'
            t+=" "
    return t


  


  
 
  plt.xlabel("x-axis")
  plt.ylabel("y-axis")
  plt.title(f"Graph of {fname(cof)}")
  plt.plot(x1,f1)
 

  plt.savefig("graph.png") 

  x1=None
  f1=None
  plt.clf()

lin=input("Enter the linspace of x: ")
func=input("Enter the coefficients of the polynomial (starting from x^0 to x^n): ")

polyplot(lin,func)
