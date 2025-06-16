class cuenta :
    def __init__(self,saldo = 1000 ):
     self.saldo = saldo
    #mostrar
    def mostrar():
       print (f"su saldo es: $"{self.saldo})
    #agregar saldo
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
    