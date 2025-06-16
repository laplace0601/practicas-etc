class cuenta :
    def __init__(self,saldo = 1000, id = 102381283180 ):
     self.saldo = saldo
     self.id = id
     
    #mostrar saldo
    def mostrar(self):
       print (f"numero de cuenta: {self.id}")
       print (f"su saldo es: ${self.saldo}")
    #mostrar saldo
    def agregar(self):
       esmeralda = input("ingrese su saldo: ")
       self.saldo += esmeralda
    #retirar saldo
    def retirar(self):
        while True:
            rubi = input("ingrese valor para retirar: ")

            if rubi > self.saldo:
                print("su valor seleccionado excede la cantidad de su cuenta")
                break
            else:
                self.saldo -= rubi
                break
caja = cuenta()
while True:
   print("bievenido a su cajero de confianza")
   print("que desea hacer ?")
   print("presione 1 si usted desea consultar saldo y numero de cuenta")
   print("2 si quiere agregar saldo")
   print("3 si quiere retirar saldo")
   print("presione cualquier otro boton para salir")
   numero = input("incertar numero: ")
   
   if numero == 1:
        caja.mostrar()
   elif numero == 2:
       caja.agregar()
   elif numero == 3:
       caja.retirar()
   else:
       print("hasta pronto :)")
       break
