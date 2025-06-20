from flask import Flask
from gema import fido
#primera aplicacion de flask
app = Flask(__name__)
@app.route('/')
def hola_mundo():
    Nombre = fido()
    return (f"hola mundo como estan {Nombre}")
if __name__ == '__main__':
    app.run(debug=True)
    