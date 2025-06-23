from flask import Flask
#importando libreria
from gema import fido
#importando funcin fido de gema.py
app = Flask(__name__)
#ruta de hola mundo
@app.route('/')
def hola_mundo():
    Nombre = fido()
    return (f"hola mundo como estan {Nombre}")
#la parte de abajo es para que se ejecute el servidor es total mente necesario

if __name__ == '__main__':
    app.run(debug=True)
    