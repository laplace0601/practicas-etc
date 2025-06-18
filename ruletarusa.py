import random
def juego():
    tambor = [False] * 5 + [True]
    random.shuffle(tambor)
    print("BIENVENIDO A LA RULETA RUSA")
    while tambor:
        
        print("presiona enter para disparar")
        intento = input()
        if tambor.pop(0): 
<<<<<<< HEAD
          print(f"PEEEEEEEEEEEERSOOOOOOOOOOOOOOOOOOOOOOOOONAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
=======
          print("PEEEEEEEEEERSOOOOOOOOOOOOOONAAAAAAAAAAAAAAAAAAAA")
>>>>>>> 0e01806c6f1f4c6dde8cf232eb626baca46f2dad
          print("BANG")
          break
        else:
         print("salvado la proxima no la cuentas")

juego()

