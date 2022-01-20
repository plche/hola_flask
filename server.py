from flask import Flask, render_template  # agregado render_template!  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    # En lugar de devolver una cadena, 
    # devolveremos el resultado del método render_template, pasando el nombre de nuestro archivo HTML
    return render_template('index.html', frase = "hola", veces = 5) # 2 nuevos argumentos nombrados!

@app.route('/success')
def success():
    return "success"

@app.route('/dojo')
def dojo():
    return "¡Dojo!"

@app.route('/hola/<name>') # para una ruta '/hola /____' cualquier cosa después de que '/hola/' se pase como una variable 'name'
def hola(name):
    print(name)
    return "Hola, " + name

@app.route('/say/<string:name>') # para una ruta '/say /____' cualquier cosa después de que '/say/' se pase como una variable 'name'
def say(name):
    return "¡Hola, " + name.capitalize() + "!"

@app.route('/users/<username>/<id>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/repeat/<int:id>/<string:name>') # para una ruta '/repeat/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def repeat(name, id):
    return (name + "<br />") * id

@app.errorhandler(404)
def page_not_found(error):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404

if __name__ == "__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug = True)    # Ejecuta la aplicación en modo de depuración