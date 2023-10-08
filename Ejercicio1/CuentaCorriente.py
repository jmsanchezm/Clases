def __init__ (self, DNI, saldo):
    self.DNI= DNI
    self.saldo = saldo
    
def __init__ (self, DNI, saldo, nombre):
    self.DNI= DNI
    self.saldo = saldo
    self.nombre = nombre
    
def sacarDinero (saldo, cantidad):
    if (saldo<=0):
        print('No se puede realizar la transacción')
    else:
        saldo-=cantidad

def ingresarDinero (saldo, cantidad):
    saldo+=cantidad
    
def __str__ (self):
    result= 'DNI:', self.DNI 
    result+= 'Nombre:', self.nombre
    result+= 'Saldo:', self.saldo
    return result

def __eq__ (self,DNI):
    result= False
    if (self.DNI== DNI):
        result=True
    return result

def __lt__ (self, saldo):
    return self.salso < saldo