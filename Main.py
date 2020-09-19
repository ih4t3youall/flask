from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

global cont = 0


@app.route('/')
def hello_world():
        return '<h1> hello</h1>'

@app.route('/julian')
def hello_juli():
    return '<h1>juli</h1>'

@app.route('/saludame')
def saludame():
    args = request.args
    nombre = args['nombre']
    return '<h1> Hola, '+nombre+'</h1>'

@app.route('/look')
def boton():
    return '<input type="button" value="Click me">'

@app.route('/getLocation',methods=['POST'])
def change_name():
    req = request.get_json()
    req[0]['direccion'] = "ramon y cajal 4060"
    req[0]['city'] ="bahia blanca"
    req[1]['direccion'] = "calle 2 numero 64"
    req[1]['city'] ="la plata"
    print(cont)
    cont
    cont = cont +1
    print(req[0]['name'])
    return jsonify(req)




if __name__ == '__main__':
    app.run('0.0.0.0',5000,debug=True)
