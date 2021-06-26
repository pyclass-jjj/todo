from flask import Flask, render_template, request, session, redirect, url_for
import model


app = Flask(__name__)
app.secret_key = "NzFiZjVjNTQzODAwYThkMWVhNGMwZWI0"

@app.route('/valida', methods=['GET'])
def valida_session():
    if 'username' in session:
        return session['username']
    else:
        return 0


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'GET':
        session.clear()
        return render_template('index.html', mensaje='Ingresa para ver tus tareas' )

    if request.method == 'POST':
        modelo = model.Modelo()
        username = request.form['username']
        password = request.form['password']
        codigo, mensaje = modelo.valida_acceso(username, password)

        if codigo == 1:
            session['username'] = username
            return redirect(url_for('tareas'))
        else:
            return render_template('index.html', mensaje=mensaje )


@app.route('/usuarios', methods=['GET'])
def lista_usuarios():

    modelo = model.Modelo()
    usuarios = modelo.get_users()

    if 'username' in session:
        print(session['username'])
        return render_template('lista_usuarios.html', lista_usuarios=usuarios, username=session['username'] )

    return render_template('lista_usuarios.html', lista_usuarios=usuarios )


@app.route('/tareas', methods=['GET'])
def tareas():

    username = valida_session()

    if username:
        modelo = model.Modelo()
        tareas = modelo.get_tareas(username)
        print(tareas)

        return render_template('tareas.html', tareas=tareas, username=username )

    else:
        return redirect(url_for('home'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'GET':
        return render_template('signup.html')

    if request.method == 'POST' and request.form['accion'] == 'signup':
        username = request.form['username']
        password = request.form['password']
        modelo = model.Modelo()
        codigo, mensaje = modelo.signup(username, password)

        if codigo == 0:
            return render_template('signup.html', mensaje=mensaje )

    return redirect(url_for('home'))

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/nueva_tarea', methods=['GET', 'POST'])
def nueva_tarea():

    username = valida_session()

    if username:

        if request.method == 'GET':
            modelo = model.Modelo()
            categorias = modelo.get_categorias()
            return render_template('nueva_tarea.html', username=username, categorias=categorias)

        if request.method == 'POST' and request.form['accion'] == 'nueva':
            modelo = model.Modelo()
            datos_nuevos = {}
            datos_nuevos['categoria'] = request.form['categoria']
            datos_nuevos['tarea'] = request.form['tarea']
            datos_nuevos['fechaini'] = request.form['fechaini']
            datos_nuevos['fechafin'] = request.form['fechafin']
            datos_nuevos['estatus'] = request.form['estatus']
            modelo.nueva_tarea(datos_nuevos, session['username'])

        return redirect(url_for('tareas'))

    else:
        return redirect(url_for('home'))


@app.route('/editar', methods=['GET', 'POST'])
def editar():

    username = valida_session()

    if username:
        if request.method == 'GET':
            id_tarea = request.args.get('id_tarea')
            modelo = model.Modelo()

            tarea = modelo.get_tareas(username, id_tarea)
            categorias = modelo.get_categorias()
            return render_template('editar.html', id_tarea=id_tarea, username=username, tarea=tarea[0], categorias=categorias)

        if request.method == 'POST' and request.form['accion'] == 'editar':
            modelo = model.Modelo()
            datos_nuevos = {}
            datos_nuevos['id_tarea'] = request.form['id_tarea']
            datos_nuevos['tarea'] = request.form['tarea']
            datos_nuevos['categoria'] = request.form['categoria']
            datos_nuevos['fechaini'] = request.form['fechaini']
            datos_nuevos['fechafin'] = request.form['fechafin']
            datos_nuevos['estatus'] = request.form['estatus']
            modelo.editar_tarea(datos_nuevos)

        return redirect(url_for('tareas'))

    else:
        return redirect(url_for('home'))


@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():

    username = valida_session()

    if username:

        if request.method == 'GET':
            id_tarea = request.args.get('id_tarea')
            return render_template('eliminar.html', id_tarea=id_tarea)

        if request.method == 'POST' and request.form['accion'] == 'eliminar':
            id_tarea = request.form['id_tarea']
            modelo = model.Modelo()
            modelo.eliminar_tarea(id_tarea)
        return redirect(url_for('tareas'))

    else:
        return redirect(url_for('home'))


@app.route('/nueva_categoria', methods=['GET', 'POST'])
def nueva_categoria():

    username = valida_session()

    if username:

        if request.method == 'GET':
            return render_template('nueva_categoria.html', username=username)

        if request.method == 'POST' and request.form['accion'] == 'nueva':
            modelo = model.Modelo()
            categoria = request.form['categoria']
            modelo.nueva_categoria(categoria)

        return redirect(url_for('tareas'))

    else:
        return redirect(url_for('home'))

    
if __name__ == '__main__':
    app.run(port=8002, debug=True)


    '''comentario prueba'''
