from flask import Flask
app = Flask(__name__)

@app.route('/saludo/<nombre>/<int:edad>')
def saludo_personalizado(nombre, edad):
    return f"¡Hola, {nombre}! Tienes {edad} años"

if __name__ == '__main__':
    app.run(debug=True)
# Este código crea una aplicación Flask que responde a una ruta personalizada