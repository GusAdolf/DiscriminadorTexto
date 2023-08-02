#IMPORTAR LIBRERIA PARA USAR FRAMEWORK FLASK
from flask import Flask, request, session, redirect, url_for, render_template, flash
from datetime import timedelta
from flask_session import Session
import os
import funciones
import bcrypt

##llamado a flask
app = Flask(__name__)

# Configuración de la sesión
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = 'sesion'
app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)

# Clave secreta para firmar las cookies de sesión
app.secret_key = 'my_secret_key'

# Inicialización de la extensión de sesión
Session(app)

# Directorio de imágenes
IMG_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

# Función para verificar las credenciales encriptadas
def verify_credentials(username, password):
    with open('credentials.txt', 'r') as file:
        credentials = file.read().split(':')
        if len(credentials) == 2:
            stored_username = credentials[0]
            stored_password_hash = credentials[1]

            if username == stored_username and bcrypt.checkpw(password.encode(), stored_password_hash.encode()):
                return True
    return False

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verificación de las credenciales de inicio de sesión
        if verify_credentials(username, password):
            session['logged_in'] = True
            session.permanent = True
            return redirect(url_for('home'))
        else:
            flash('Credenciales incorrectas')
    
    return render_template('login.html')




@app.route('/', methods = ["GET","POST"])
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    fondoP = os.path.join(app.config['UPLOAD_FOLDER'], 'fondo.webp')
    sale = os.path.join(app.config['UPLOAD_FOLDER'], 'salesiana.png')
    log1 = os.path.join(app.config['UPLOAD_FOLDER'], 'ingles.svg')
    log2 = os.path.join(app.config['UPLOAD_FOLDER'], 'LG1_ingles.svg')
    return render_template('index.html',fondo=fondoP,sale=sale,logo1=log1,logo2=log2)

@app.route('/about', methods = ["GET","POST"])
def about():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    sale = os.path.join(app.config['UPLOAD_FOLDER'], 'salesiana.png')
    log1 = os.path.join(app.config['UPLOAD_FOLDER'], 'ingles.svg')
    log2 = os.path.join(app.config['UPLOAD_FOLDER'], 'LG1_ingles.svg')
    gus = os.path.join(app.config['UPLOAD_FOLDER'], 'gus.jpg')
    
    alexis = os.path.join(app.config['UPLOAD_FOLDER'], 'alexis.jpeg')
    
    return render_template('info.html', g=gus, a=alexis, sale=sale,logo1=log1,logo2=log2)

@app.route('/procesar', methods = ["GET","POST"])
def procesar():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    sale = os.path.join(app.config['UPLOAD_FOLDER'], 'salesiana.png')
    log1 = os.path.join(app.config['UPLOAD_FOLDER'], 'ingles.svg')
    log2 = os.path.join(app.config['UPLOAD_FOLDER'], 'LG1_ingles.svg')
    return render_template('procesar.html', sale=sale,logo1=log1,logo2=log2)



#Frase

@app.route('/result',methods=['POST',"GET"] )
def result ():
    output= request.form.to_dict()
    texto=output["frase"]
    #archivo=output["archivo"]
    
    if(texto!=""):
        norm=funciones.discriminatorio1(texto)
        norm2=funciones.discriminatorio2(texto)
        eda = os.path.join(app.config['UPLOAD_FOLDER'], 'edad.jpg')
        raz = os.path.join(app.config['UPLOAD_FOLDER'], 'raza.jpg')
        gen = os.path.join(app.config['UPLOAD_FOLDER'], 'genero.jpg')
        ori = os.path.join(app.config['UPLOAD_FOLDER'], 'orientacion.jpg')
        nodis = os.path.join(app.config['UPLOAD_FOLDER'], 'nada.jpg')
        pos = norm2[3]
        pos2 = norm[2]
        generos = [raz,gen,ori,eda,nodis]
    
        print(norm2)
        ups = os.path.join(app.config['UPLOAD_FOLDER'], 'salesiana.png')
        log1 = os.path.join(app.config['UPLOAD_FOLDER'], 'ingles.svg')
        log2 = os.path.join(app.config['UPLOAD_FOLDER'], 'LG1_ingles.svg')
        return render_template("procesar.html",logo1=log1,logo2=log2,sale=ups, norm=norm[1],norm3=norm2[1],texto=texto,image=generos[pos],image2=generos[pos2],pos1=pos,pos2=pos2)
 
    norm=funciones.normalizar(texto)
    
   
    
    
    

##ejecutar el servicio web
if __name__=='__main__':
    #OJO QUITAR EL DEBUG EN PRODUCCION
    app.run(host='0.0.0.0', port=5000, debug=True)


