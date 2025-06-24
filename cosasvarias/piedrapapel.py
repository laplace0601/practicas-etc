import random
opciones = ["piedra", "papel" , "tijera"]
def juego ():
    print (" escoge")
    print ("piedra, papel , o tijera")
    uso = input("selecciona: ").lower() 
    computadora = random.choice(opciones)
    if uso == computadora:
        print("EMPATE")
    elif (uso == "piedra" and computadora == "tijera") or (uso == "papel" and computadora == "piedra") or (uso == "tijera" and computadora == "papel"):
        print("GANAAAAAAAAAAAAAAAAAAAAAAAAASSSSSSSSSSSSSSSSTEEEEEEEEEEEEEEEEEEEEEEE")
    elif uso not in opciones:
        print("wtf escoge bien animal")
    else:
        print("perdiste :( ")

juego()