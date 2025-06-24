from time import sleep
try:
    segundos = float(input("incerte la cantidad de tiempo en segundos: "))

    while segundos > 0:
        segundos -= 1
        sleep(1)
        print(f"quedan {segundos} segundos")

    print("SE ACABO EL TIEMPO")
except ValueError:
    print("por favor coloque un numero positivo")