#la hice en lambda porque no necesitan mucho espacio
suma = lambda num1, num2 : num1 + num2
resta = lambda num1, num2 : num1 - num2
multiplicacion = lambda num1, num2 : num1 * num2
#esta tambien se puede hacer lambda pero me gusta mas asi
def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("wtf quien intenta dividir entre 0, es como que ella te ame bro , simplemente no se puede")


