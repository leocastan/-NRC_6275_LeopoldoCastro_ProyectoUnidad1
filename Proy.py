# Importar la biblioteca de flask y librerias necesarias
from tkinter import messagebox
from flask import Flask, render_template


# Instanciar la aplicación
# Nombre por defecto y ruta donde están los modelos
app = Flask(__name__)


# 1. Funcion controlador que muestra la página principal del sitio
# Definicion de la ruta por defecto,
@app.route('/')
# Lamar a principal
def index():
    '''Esta funcion muestra la página principal del sitio'''
    return render_template('index.html')

print("Nombre de la funcion: ",index.__name__)
print("Documentacion: ",index.__doc__)

# 2. Funcion controlador que muestra la página autoridades
# Definicion de la ruta por defecto,
@app.route('/autoridades')
# Lamar a principal
def autoridades():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('autoridades.html')

# 3. Funcion controlador que muestra la página autoridades
# Definicion de la ruta por defecto,
@app.route('/actividadesFuturas')
# Lamar a principal
def actividadesFuturas():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('actividadesFuturas.html')

# 3. Funcion controlador que muestra la página autoridades
# Definicion de la ruta por defecto,
@app.route('/conocenos')
# Lamar a principal
def conocenos():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('conocenos.html')

# 3. Funcion controlador que muestra la página autoridades
# Definicion de la ruta por defecto,
@app.route('/contacto')
# Lamar a principal
def contacto():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('contacto.html')

# 3. Funcion controlador que muestra la página autoridades
# Definicion de la ruta por defecto,
@app.route('/galeriaDirectores')
# Lamar a principal
def galeriaDirectores():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('galeriaDirectores.html')

# 3. Funcion controlador que muestra la página autoridades
# Definicion de la ruta por defecto,
@app.route('/galeriaImagenes')
# Lamar a principal
def galeriaImagenes():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('galeriaImagenes.html')

# 3. Funcion controlador que muestra la página autoridades
# Definicion de la ruta por defecto,
@app.route('/mision')
# Lamar a principal
def mision():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('mision.html')

# 3. Funcion controlador que muestra la página autoridades
# Definicion de la ruta por defecto,
@app.route('/noticias')
# Lamar a principal
def noticias():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('noticias.html')

# 3. Funcion controlador que muestra la página autoridades
# Definicion de la ruta por defecto,
@app.route('/objetivosInstitucionales')
# Lamar a principal
def objetivosInstitucionales():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('objetivosInstitucionales.html')

# 3. Funcion controlador que muestra la página autoridades
# Definicion de la ruta por defecto,
@app.route('/politicasPrivacidad')
# Lamar a principal
def politicasPrivacidad():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('politicasPrivacidad.html')

# 3. Funcion controlador que muestra la página autoridades
# Definicion de la ruta por defecto,
@app.route('/quito')
# Lamar a principal
def quito():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('quito.html')

# 3. Funcion controlador que muestra la página autoridades
# Definicion de la ruta por defecto,
@app.route('/sangolqui')
# Lamar a principal
def sangolqui():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('sangolqui.html')


# 3. Funcion controlador que muestra la página autoridades
# Definicion de la ruta por defecto,
@app.route('/vision')
# Lamar a principal
def vision():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('vision.html')


# Metodo main del programa
if __name__ == '__main__':
    # debug = True, para reiniciar automatica el servidor
    app.run(debug=True)
