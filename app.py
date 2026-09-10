from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a MySQL
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # Cambia según tus credenciales
        password="",        # Cambia según tus credenciales
        database="medio_ambiente"
    )

@app.route('/')
def index():
    # Estructura básica lista para futuras consultas a la BD
    try:
        conexion = conectar_db()
        # Aquí puedes realizar consultas SQL si lo necesitas más adelante
        conexion.close()
    except mysql.connector.Error as err:
        print(f"Nota: No se pudo conectar a MySQL: {err}")
        
    return render_template('index.htm')

# Ruta agregada para cargar la plantilla de la trivia
@app.route('/trivia')
def trivia():
    return render_template('trivia.htm')

if __name__ == '__main__':
    app.run(debug=True)