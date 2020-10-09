from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL
app = Flask(__name__)

app.config["DEBUG"] = True


app.config['MYSQL_DATABASE_USER'] = 'sepherot_roberto'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Fe2zrCW7b3'
app.config['MYSQL_DATABASE_DB'] = 'sepherot_robertoBD'
app.config['MYSQL_DATABASE_HOST'] = 'nemonico.com.mx'
mysql = MySQL(app)

    
def insertarEventoP(_name,_password,_rfc, _email,_direccion,_fechanacimiento,_estadocivil):
    try:
       
        if _name and _password and _rfc and _email and _direccion and _fechanacimiento and _estadocivil:
            conn = mysql.connect()
            cursor = conn.cursor()
            print("paso 1")
            _TABLA="T_UserPoints"
            sqlDropProcedure="DROP PROCEDURE IF EXISTS InsertUsers;"
            print("paso 2")
            cursor.execute(sqlDropProcedure)
            print("paso 3")
            sqlCreateSP="CREATE PROCEDURE InsertUsers(IN UName VARCHAR(50), IN UEmail VARCHAR(50), IN UPass VARCHAR(50), IN UAdd VARCHAR(50), IN UDate DATE, IN URFC VARCHAR(50), IN CStatus VARCHAR(50), IN UStatus INT(20)) INSERT INTO "+_TABLA+"(UName, UEmail, UPass, UAdd, UDate, URFC, CStatus, UStatus) VALUES (UName, UEmail, UPass, UAdd, UDate, URFC, CStatus, UStatus)"
            print("paso 4")
            cursor.execute(sqlCreateSP)
            print("paso 5")
            cursor.execute("CREATE TABLE IF NOT EXISTS `sepherot_robertoBD`.`"+_TABLA+"` (`UName` VARCHAR(50) NOT NULL, `UEmail` VARCHAR(50) NOT NULL , `UPass` VARCHAR(50) NOT NULL ,`UAdd` VARCHAR(50) NOT NULL,`UDATE` DATE NOT NULL,`URFC` VARCHAR(50) NOT NULL,`CStatus` VARCHAR(50) NOT NULL,`UStatus` INT(20),`Tiempo` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (`IdUsers`)) ENGINE = InnoDB;")                    
            #cursor.execute("INSERT INTO `T_UserPoints` (`UName`,`UEmail`,`UPass`,`UAdd`,`UDATE`,`URFC`,`CStatus`) VALUES (%s, %s, %s, %s)",(_n, _l, _e, _p))
            print("paso 6")
            cursor.callproc('InsertUsers',(_name, _email , _password, _direccion, _fechanacimiento, _rfc, _estadocivil,1))
            print("paso 7")
            data = cursor.fetchall()
            

            if len(data)==0:
                conn.commit()
                print("se registro?")
                return json.dumps({'message':'Evento registrado correctamente !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            print("error")
            return json.dumps({'html':'<span>Datos faltantes</span>'})

    except Exception as e:
        print("error 2")
        print(json.dumps({'error':str(e)}))
        return json.dumps({'error':str(e)})
    finally:
       cursor.close() 
       print("cierre")
       conn.close()
         
     


