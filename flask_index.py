#Importar el módulo Flask en el proyecto.
from flask import Flask, render_template

#Crear un objeto de la clase Flask.
app = Flask(__name__)

#La función route() de la clase Flask.
@app.route("/student")

#‘/’ URL está vinculado con la función first_flask.
def student_webpage():

    name = 'Choba'
    return render_template('student.html', student_name = name)
app.run(debug=True)