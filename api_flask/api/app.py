from flask import Flask
from flask import render_template, jsonify, request, redirect, url_for
import json
from connectiondb import connect_db, get_list
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Retorna la pagina index."""
    print("OK")
    if(request.method == 'GET'):
        con = connect_db()

        lista = get_list("personajes")
    return render_template('/index.html', datos=lista)

@app.route('/cargar')
def cargar():
    dic = {'nombre': '', 'aparicion': '', 'biografia': '', 'personaje': ''}
    return render_template('/cargar.html', documento=dic)


@app.route('/about')
def about():
    """Retorna la pagina about."""
    return render_template('/about.html', msj="About de la pagina")



if __name__ == '__main__':
    app.run(host='web-app-flask', port='5000', debug=True)