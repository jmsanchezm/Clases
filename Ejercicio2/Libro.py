def __init__(self, titulo,autor,numEjemplares,numPrestados):
    self.titulo= titulo
    self.autor=autor
    self.numEjemplares=numEjemplares
    if numPrestados>numEjemplares:
        numPrestados=0
    else:
        self.numPrestados=numPrestados
    
def prestamo(self):
    result=False
    if self.numPrestados < self.numEjemplares:
        self.numPrestados+=1
        result=False
    
    return result
        
        
def devolucion ():
    result=False
    if numPrestados>0:
        result=True
        numPrestados-=1
    
    return result

def __str__(self):
    result= 'Titulo:', self.titulo
    result+='Autor:', self.autor
    result+= 'Número de ejemplares:', self.numEjemplares
    result+= 'Número de libros prestados:', self.numPrestados
    
    return result
    
def __eq__(self, titulo, autor):
    result = False
    if self.titulo == titulo and self.autor==autor:
        result = True
        
    return result

def __lt__ (self, autor):
    return self.autor < autor