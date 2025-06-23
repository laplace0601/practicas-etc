from flask import Flask
#importando libreria flask
#en este caso no es necesario importar gema.py ya que no se usa
#pero si se quisiera usar se importaria de la misma manera que en pract1.py
#de hecho se puede importar cualquier libreria de python
#y usarla en flask como si fuera un programa normal de python
#app
app = Flask (__name__)
@app.route('/')
def menu():
    #ruta del menu recuerda no es necesario usar print aqui en flask
    #ya que se imprime en el navegador

    return ('hola, bienvenido al menu principal') #y no en la terminal
@app.route('/introducion')
def introducion():
     #en este caso se imprime el menu principal  
    return ('hola introducion a flask')
@app.route('/desarrollo')
def desarrollo():
    return ('estoy practicando flask')
@app.route('/despedida')
def despedida():
    return ('adios, hasta la proxima')
#parte necesaria para que se ejecute el servidor
#recuerda que si no se pone esto no se ejecuta el servidor
#y no se ve en el navegador 
if __name__ == '__main__':
    app.run(debug=True)
    