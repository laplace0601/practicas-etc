from flask import Flask, render_template
#render_template permite renderizar una plantilla HTML
#en este caso, se usara la plantilla saludo.html    

app= Flask(__name__)
@app.route('/saludo/<nombre>')
def saludo_personalizado(nombre):
    #aqui se esta llamando a la plantilla saludo.html
    #y se le pasa el nombre como variable
    #la plantilla saludo.html debe estar en la carpeta templates    
    return render_template('saludo.html', nombre=nombre)
