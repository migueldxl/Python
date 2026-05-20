from flask import Flask, render_template

app = Flask(__name__)

@app.route('/usuario')
def usuario():
    return render_template('usuario.html', nome="Carlos", idade=28)

@app.route('/perfil')
def perfil():
    usuario_dados = {"nome": "Ana", "email": "ana@email.com"}
    return render_template('perfil.html', usuario=usuario_dados)

@app.route('/alunos')
def lista_alunos():
    lista_nomes = ["Bruno", "Ana", "Diego", "Amanda"]
    nota_aluno = 7.5
    
    return render_template(
        'alunos.html', 
        alunos=lista_nomes, 
        nota=nota_aluno
    )
@app.route('/')
def home():
    return "<h1>Bem-vindo! Escolha uma rota: /usuario, /perfil ou /alunos</h1>"
if __name__ == '__main__':
    app.run(debug=True)
