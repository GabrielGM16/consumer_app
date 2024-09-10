from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__)

# Ruta para la página principal que muestra el formulario
@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Recoge las respuestas del formulario
        name = request.form['name']
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']
        q6 = request.form['q6']
        q7 = request.form['q7']

        # Guarda las respuestas en un archivo CSV
        save_responses(name, q1, q2, q3, q4, q5, q6, q7)

        return redirect('/thankyou')

    return render_template('form.html')

# Ruta de la página de agradecimiento
@app.route('/thankyou')
def thank_you():
    thank_you_page = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gracias</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #121212;
                color: #FFFFFF;
                text-align: center;
                padding: 40px;
            }
            h1 {
                color: #00FF00;
                font-size: 2.5rem;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.5rem;
                color: #00FFFF;
            }
            a {
                color: #00FF00;
                text-decoration: none;
                font-size: 1.2rem;
                margin-top: 20px;
                display: inline-block;
                background-color: #1F1F1F;
                padding: 10px 15px;
                border-radius: 5px;
            }
            a:hover {
                background-color: #00FFFF;
                color: #000000;
            }
        </style>
    </head>
    <body>
        <h1>¡Gracias por tu participación!</h1>
        <p>Tu respuesta ha sido guardada correctamente.</p>
        <a href="/">Volver al inicio</a>
    </body>
    </html>
    '''
    return thank_you_page


# Función para guardar las respuestas en un archivo CSV
def save_responses(name, q1, q2, q3, q4, q5, q6, q7):
    # Verifica si el archivo CSV ya existe
    file_path = 'data/responses.csv'
    if not os.path.exists(file_path):
        # Si no existe, crea el archivo con encabezados
        df = pd.DataFrame(columns=['Nombre', 'Pregunta 1', 'Pregunta 2', 'Pregunta 3', 'Pregunta 4', 'Pregunta 5', 'Pregunta 6', 'Pregunta 7'])
        df.to_csv(file_path, index=False)

    # Agrega las nuevas respuestas al archivo CSV
    new_data = pd.DataFrame([[name, q1, q2, q3, q4, q5, q6, q7]], 
                            columns=['Nombre', 'Pregunta 1', 'Pregunta 2', 'Pregunta 3', 'Pregunta 4', 'Pregunta 5', 'Pregunta 6', 'Pregunta 7'])
    new_data.to_csv(file_path, mode='a', header=False, index=False)

if __name__ == '__main__':
    app.run(debug=True)
