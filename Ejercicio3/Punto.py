import math

def __init__ (self, x,y):
    self.x=x
    self.y=y
    
def __str__ (self):
    return '('+ self.x +',' + self.y +')'

def setXY (self,x,y):
    self.x=x
    self.y=y
    
def desplaza (self,dx,dy):
    self.x=dx
    self.y=dy
    
    print ('('+ self.x +',' + self.y +')')
    
def distancia (Punto,self):
    distancia=0
    distancia= math.sqrt(((Punto.x-self.x)*(Punto.x-self.x))+((Punto.y-self.y)*(Punto.y-self.y)))
    
    return distancia