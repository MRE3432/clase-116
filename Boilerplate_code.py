#Importar el módulo Flask en el proyecto.
from flask import Flask

#Crear un objeto de la clase Flask.
app = Flask("/flask2")

#La función route() de la clase Flask.
@app.route("/")

#‘/’ URL está vinculado con la función first_flask.
def first_flask():

    return "Este es mi primer programa en Flask"

#Ejecutamos la app en el servidor local.
@app.route("/flask3")
def third_flask():
    return "la choba es obetsa"
app.run(debug=True)