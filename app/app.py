from flask import Flask, render_template, request, url_for, redirect


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
    return render_template('index.html',data=data)

@app.route('/scrapers/<area>')
def scrapers(area):
    data={
        'title':'Index',
        'msg': area,
        'param': request.args.get('param1')
    }
    return render_template('scrapers.html',data=data)

# Página no encontrada
def page_not_found(error):
    data={
        'title':'Error',
        'msg': error
    }
    return render_template('404.html',data=data), 404
    # print(error)
    # return redirect(url_for('index'))

if __name__=='__main__':
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)