class cuenta :
    def __init__(self,saldo = 1000, id = 102381283180 ):
     self.saldo = saldo
     self.id = id
     
    #mostrar saldo
    def mostrar(self):
       print (f"numero de cuenta: {self.id}")
       print (f"su saldo es: ${self.saldo}")
    def agregar(self):
       esmeralda = float(input("ingrese su saldo: "))
       self.saldo += esmeralda
       # retirar saldo
    def retirar(self):
        while True:
            rubi = float(input("ingrese valor para retirar: "))
        #condicional para evitar que saquen mas saldo de lo que ya se tiene
            if rubi > self.saldo:
                print("su valor seleccionado excede la cantidad de su cuenta")
                break
            else:
                self.saldo -= rubi
                break
    
caja = cuenta()
#interfaz del banco
def cajabank():
    while True:
        print("bievenido a su cajero de confianza")
        print("1 consultar saldo y numero de cuenta")
        print("2  agregar saldo")
        print("3 retirar saldo")
        print("presione cualquier otro boton para salir")
        numero = float(input("incertar numero: "))
        if numero == 1:
                caja.mostrar()
        elif numero == 2:
            caja.agregar()
        elif numero == 3:
            caja.retirar()
        else:
            print("hasta pronto :)")
            break
        
        
#iniciar interfaz
cajabank()