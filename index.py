from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    print("Hola")
    return render_template('home.html')


@app.route('/about')
def about():
     return render_template('about.html')

@app.route('/user')
def user():
    return render_template('user.html')

     
@app.route('/adduser', methods = ['POST', 'GET'])
def adduser():
     adduser = request.form
     email = request.args["Email"]
     password = request.args["password"]
     nacionalidad = request.args["nacionalidad"]
     ciudadactual = request.args["ciudadactual"]
     celular = request.args["celular"]
     visitantes = request.args["visitantes"]
     estadia = request.args["estadia"]
     motivaciones = request.args["motivaciones"]
     preferencias = request.args["preferencias"]
     return render_template ('adduser.html', email = email, nacionalidad = nacionalidad, ciudadactual = ciudadactual, celular = celular, visitantes=visitantes, estadia=estadia, motivaciones=motivaciones, preferencias=preferencias)

@app.route('/empresa')
def empresa():
     return render_template ('empresa.html')

@app.route('/addempresa', methods=['POST', 'GET'])
def addempresa():
     addempresa = request.form
     email = request.args["email"]
     password = request.args["password"]
     rut = request.args["RUT"]
     return render_template ('addempresa.html', email = email, password = password, rut = rut)

if __name__ == '__main__':
    app.run(debug=True)







