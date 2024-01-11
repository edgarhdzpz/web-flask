from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Lista para almacenar los comentarios (simulando una "base de datos" en memoria)
comentarios = []

# Otras rutas de tu aplicación

@app.route('/guardar_comentario', methods=['POST'])
def guardar_comentario():
    nombre = request.form.get('nombre')
    comentario_texto = request.form.get('comentario')

    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Crear un diccionario con la información del comentario
    nuevo_comentario = {
        'nombre': nombre,
        'comentario': comentario_texto,
        'fecha': fecha_actual
    }

    # Agregar el nuevo comentario a la lista
    comentarios.append(nuevo_comentario)

    # Redirigir a la página principal después de procesar el comentario
    return redirect(url_for('feedback'))

# @app.route('/')
# def index():
#     return render_template('index.html', comentarios=comentarios)

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/feedback")
def feedback():
    return render_template('feedback.html', comentarios=comentarios)

# bloque de prueba
if __name__ == '__main__':
    app.run(debug=True)