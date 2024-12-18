from flask import *
app = Flask(__name__)

users = [['claudio','12345','Claudio Macena']
    ,['mari','9876','Lara Mariane'],
     ['pedro','teste1','Pedro Inácio']]

app.secret_key = 'ASDdagsd@1'


@app.route('/logout', methods=['POST', 'GET'])
def sair():
    session.pop('login')
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def pag_principal():
    return render_template('index.html')

@app.route('/minhasfofocas')
def pag_fofoca():
    if 'login' in session:
        return render_template('fofocas.html')
    else:
        return render_template('index.html')

@app.route('/fazerlogin', methods=['POST'])
def fazer_login():
    login_user = request.form.get('login')
    senha_user = request.form.get('senha')
    logado = False
    for usuario in users:
        if usuario[0] == login_user and usuario[1] == senha_user:
            nome_logado = usuario[2]
            session['login'] = login_user
            logado = True
            break

    if logado == True:
        return render_template('home.html', nome=nome_logado)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
