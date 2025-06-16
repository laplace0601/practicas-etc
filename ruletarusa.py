import random
def juego():
    tambor = [False] * 5 + [True]
    random.shuffle(tambor)
    while tambor:
        print("BIENVENIDO A LA RULETA RUSA")
        print("presiona enter para disparar")
        intento = input()
        if tambor.pop(0): 
          print(f"PEEEEEEEEEEEERSOOOOOOOOOOOOOOOOOOOOOOOOONAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
          print("BANG")
          break
        else:
         print("salvado la proxima no la cuentas")

juego()

