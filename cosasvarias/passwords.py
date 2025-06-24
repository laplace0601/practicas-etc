from random import choice
import string
longitud = int(input("elige la longitud de tu contraseña: "))
caracteres = string.ascii_letters + string.digits  + string.punctuation
contrasena = '' 

for _ in range(longitud):
   contrasena += choice(caracteres)


print(f"su contraseña es: {contrasena}")   