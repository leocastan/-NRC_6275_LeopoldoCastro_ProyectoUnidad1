# Importar la biblioteca de flask y librerias necesarias
from tkinter import messagebox
from flask import Flask, redirect, render_template, request, url_for, flash
import pickle

# Instanciar la aplicación
# Nombre por defecto y ruta donde están los modelos
app = Flask(__name__)


# 1. Funcion controlador que muestra la página principal del sitio
# Definicion de la ruta por defecto,
@app.route('/')
# Lamar a principal
def principal():
   # '''Esta funcion muestra la página principal del sitio'''
    return render_template('principal.html')

#print("Nombre de la funcion: ",principal.__name__)
#print("Documentacion: ",principal.__doc__)




# Metodo main del programa
if __name__ == '__main__':
    # debug = True, para reiniciar automatica el servidor
    app.run(debug=True)
