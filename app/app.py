from flask import Flask, render_template, request, url_for, redirect, jsonify
import urllib.request, json
import os
app=Flask(__name__)

# Ejecuta la función antes de una petición
@app.before_request
def before_request():
    print("Antes de la petición...")

# Ejecuta la función despues de una petición
@app.after_request
def after_request(response):
    print("Despues de la petición...", response)
    return response

@app.route('/')
def index():
    data={
        'title':'Index',
        'msg': 'Bienvenido al sitio'
    }
    return data

@app.route('/scrapers/<area>')
def scrapers(area):
    data={
        'title':'Index',
        'msg': area,
        'param': request.args.get('param1')
    }
    return data

@app.route("/test")
def get_movies():
    url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(os.environ.get("TMDB_API_KEY"))

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template ("movies.html", movies=dict["results"])

# Página no encontrada
def page_not_found(error):
    data={
        'title':'Error',
        'msg': str(error)
    }
    return data

if __name__=='__main__':
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)