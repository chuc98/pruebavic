from flask import Flask, render_template, request, json, url_for, redirect,send_from_directory, g, session
import os
#from PyPDF2 import PdfFileReader
from werkzeug.utils import secure_filename
from pathlib import Path
import Modelo as Modelo
import time
import re
import jinja2

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] ='Archivos'
app.config['UPLOAD_EXTENSIONS'] = '.pdf'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.before_request
def before_request():
   g.user = None
   if 'user' in session:
      g.user = Modelo.buscarU(session['user'])

@app.route("/")
def index():
   return render_template("./inicialekko.html")

@app.route('/B',methods= ['POST','GET'])
def B():
        f=request.files['archi']
        filename= secure_filename(f.filename)
        usuario=f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return "<h1>Archivo Subido Exitosamente </h1>" 
        user=request.form['archi']
        if usuario == True:
           session['user'] = user 
           Modelo.entities(user, 'subir contrato', 'Se subio el contrato exitosamente')
           return redirect(url_for('logeado'))
        else:
            errorlog= "Te faltan campos"
            Modelo.entities(user, 'Error al subir contrato', 'No se pudo subir el contrato')
            return render_template('logeado.html', errorlog = errorlog) 
  


@app.route("/registro",methods=['GET', 'POST'])
def insertarEventoP():
    if request.method == 'POST':
        _name=request.form.get('DName')
        _email=request.form.get('DEmail')
        _password=request.form.get('DPassword')
        _direccion=request.form.get('DDireccion')
        _fechanacimiento=request.form.get('DEdad')
        _rfc=request.form.get('DRFC')
        _estadocivil=request.form.get('DEstadoCivil')
        usuario = Modelo.insertarEventoP(_name,_password,_rfc, _email,_direccion,_fechanacimiento,_estadocivil)
        user=request.form['DEmail']
        if usuario == True:
           session['user'] = user 
           Modelo.entities(user, 'registrarse', 'El usuario se registro')
           return redirect(url_for('index'))
        else:
            errorlog= "Te faltan campos"
            Modelo.entities(user, 'Error al registrarse', 'No pudo registrarse')
            return render_template('registro.html', errorlog = errorlog)
     
               
    return render_template ("./registro.html")

              

      




@app.route("/login",methods=['GET', 'POST'])
def log():
   
   if g.user:
         return redirect(url_for('logea'))
   if request.method=='POST':
         session.pop('user', None)
         
      
         user=request.form['LEmail']
         password= request.form['LPassword']
         if (user and password):
            usuario= Modelo.validarUsuario(user,password)
            if usuario == True:
               session['user'] = user 
               Modelo.entities(user, 'Login', 'El usuario hizo log')
               return redirect(url_for('logea'))
            else:
               errorlog = "Tus datos son incorrectos"
               Modelo.entities(user, 'Login.Fail.NotFound', "Ingreso mal sus datos")
               return render_template('login.html',errorlog = errorlog)   
   return render_template('login.html')
 




@app.route("/logeado")
def logea():
   return render_template("./logeado.html")


@app.route("/actualizar")
def ActualizarEventoP():

   return render_template("./actualizar.html")
        

if __name__ == "__main__":
    app.run()   
