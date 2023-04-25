#IMPORTAR LIBRERIA PARA USAR FRAMEWORK FLASK
from flask import Flask,request, session, redirect, url_for
from flask import render_template
import os
from flask import request
import pymysql
import funciones
##llamado a flask
app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'img')
app.secret_key = 'my_secret_key'

app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/', methods = ["GET","POST"])
def home():
    fondoP = os.path.join(app.config['UPLOAD_FOLDER'], 'fondo.png')
    return render_template('index.html',fondo=fondoP)

@app.route('/about', methods = ["GET","POST"])
def about():
    
    gus = os.path.join(app.config['UPLOAD_FOLDER'], 'gus.jpg')
    
    alexis = os.path.join(app.config['UPLOAD_FOLDER'], 'alexis.jpeg')
    
    return render_template('info.html', g=gus, a=alexis)

@app.route('/procesar', methods = ["GET","POST"])
def procesar():
    
    return render_template('procesar.html')



#Frase

@app.route('/result',methods=['POST',"GET"] )
def result ():
    output= request.form.to_dict()
    texto=output["frase"]
    #archivo=output["archivo"]
  
    if(texto!=""):
        norm=funciones.discriminatorio1(texto)
        norm2=funciones.discriminatorio2(texto)
        return render_template("procesar.html",norm=norm,norm2=norm2[0],norm3=norm2[1],norm4=norm2[2],texto=texto)
 
    """"elif(archivo!=""):
        norm=funciones.discriminatorio1(archivo)
        norm2=funciones.discriminatorio2(archivo)
    
        return render_template("procesar.html",norm=norm,norm2=norm2[0],norm3=norm2[1],norm4=norm2[2],texto=archivo)
    """
    norm=funciones.normalizar(texto)

##ejecutar el servicio web
if __name__=='__main__':
    #OJO QUITAR EL DEBUG EN PRODUCCION
    app.run(host='0.0.0.0', port=5000, debug=True)


