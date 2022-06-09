# Importar la biblioteca de flask y librerias necesarias
from copyreg import pickle
from tkinter import messagebox
from flask import Flask, redirect, render_template, url_for, request



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
@app.route('/ingresoNotas')
# Lamar a principal
def ingresoNotas():
    '''Esta funcion muestra la página autoridades del sitio'''
    return render_template('ingresoNotas.html')

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


# Arreglo para almacenar las tareas
listaTareas = []

# 1. Funcion controlador que muestra lista actual de tareas pendientes y un formulario para ingresar un nuevo elemento
# Definicion de la ruta por defecto,
@app.route('/ingreso')
# Lamar a principal
def ingreso():
    return render_template('ingreso.html', listaTareas=listaTareas)

# 2. Funcion controlador para agregar lista a tarea de pendientes
# Definicion de la ruta
@app.route('/enviar', methods=['POST'])
# Llamar a enviar
def enviar():
    # Funcion condicional para enviar los datos del formulario
    if request.method == 'POST':

        estudiante = request.form['estudiante']
        asignatura = request.form['asignatura']
        calificacion = request.form['calificacion']

        # Funcion condicional para no registrar en caso de datos vacios
        if estudiante == '' or asignatura == '' or calificacion == '':
            #Mensaje de alerta de campos faltantes
            messagebox.showwarning("¡Alerta!","Ingrese todos los campos")
            return redirect(url_for('ingreso'))

        else:
            #Mensaje de autorizacion de registro
            resultado = messagebox.askquestion("Registrar", "¿Está seguro que desea registrar los datos?")
            #Funcion condicional de confirmacion de registro
            if resultado == "yes":
                listaTareas.append({'estudiante': estudiante, 'asignatura': asignatura, 'calificacion': calificacion })
                return redirect(url_for('ingreso'))
            else:
                return redirect(url_for('ingreso'))

# 3. Funcion controlador para borrar la lista de tareas
@app.route('/borrar', methods=['POST'])
def borrar():
    if request.method == 'POST':
        # Funcion condicional para mostrar alerta en caso de no existir
        if listaTareas == []:
            messagebox.showwarning("¡Alerta!", "No existen tareas pendientes")
            return redirect(url_for('ingreso'))
        else:
            # Mensaje de autorizacion de borrado
            resultado = messagebox.askquestion(
                "Borrar datos", "¿Está seguro de que desea borrar los datos?")
            # Funcion condicional de confirmacion de borrado
            if resultado == "yes":
                messagebox.showinfo("Info", "Los datos han sido borrados")
                listaTareas.clear()
                return redirect(url_for('ingreso'))
            else:
                return redirect(url_for('ingreso'))

# 4. Funcion controlador para guardar registros en archivo *.pickle
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        # Funcion condicional para mostrar alerta en caso de no existir
        if listaTareas == []:
            messagebox.showwarning(
                "¡Alerta!", "No existen tareas para almacenar")
            return redirect(url_for('ingreso'))
        else:
            # Mensaje de autorizacion de guardado
            resultado = messagebox.askquestion(
                "Guardar registros", "¿Está seguro de que desea guardar los datos?")
            # Funcion condicional de confirmacion de guardado
            if resultado == "yes":
                # Funcion de creacion y sobreescritura de archivo *.pickle
                with open('Tareas.pickle', 'wb') as f:
                    tareas = {'tareas': listaTareas}
                    pickle.dump(tareas, f)
                messagebox.showinfo("Info", "Los datos han sido guardados")
                return redirect(url_for('ingreso'))
            else:
                return redirect(url_for('ingreso'))



# Metodo main del programa
if __name__ == '__main__':
    # debug = True, para reiniciar automatica el servidor
    app.run(debug=True)
