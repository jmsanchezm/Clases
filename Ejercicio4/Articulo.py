IVA = 21

def __init__ (self, nombre, precio, cuantosQuedan):
    self.nombre = nombre
    self.precio = precio
    self.cuantosQuedan = cuantosQuedan
    
def getPVP (self):
    return (self.precio * IVA) + self.precio

def getPVPDescuento(self, descuento):
    descuento=descuento/100
    precioDesc = self.precio*descuento-self.precio
    return precioDesc

def vender (self,cant):
    result=False
    if cant<self.cuantodQuedan:
        result=True
        self.cuantosQuedan-=cant
    
    return result

def almacenar (self, cant):
    self.cuantosQuedan+=cant
    print('Operación realizada')
    
def __init__ (self):
    result='Nombre:', self.nombre
    result+='Precio:', self.precio
    result+= 'Stock:', self.cuantosQuedan 
    
    return result

def __eq__ (self,nombre):
    result=False
    if self.nombre==nombre:
        result=True
    return result

def __lt__ (self, nombre):
    return self.nombre<nombre