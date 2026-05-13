from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    dados = {
        "nome": "Seu Nome Completo",
        "telefone": "(31) 99999-9999",
        "email": "seu.email@email.com",
        "educacao": [
            {"instituicao": "Universidade Exemplo", "curso": "Ciência da Computação", "periodo": "2022 - 2026"},
            {"instituicao": "Escola Técnica Alfa", "curso": "Ensino Médio Técnico", "periodo": "2019 - 2021"}
        ],
        "experiencia": [
            {"empresa": "Empresa Tech", "cargo": "Desenvolvedor Júnior", "periodo": "2024 - Presente", "atividades": "Desenvolvimento de APIs e manutenção de sistemas."},
            {"empresa": "Inova Start", "cargo": "Estagiário", "periodo": "2023 - 2024", "atividades": "Suporte ao time de desenvolvimento e testes de software."}
        ],
        "cursos": [
            "Python Impressionador - Hashtag Treinamentos",
            "Flask Web Development - Udemy",
            "Metodologias Ágeis Scrum - Coursera"
        ],
        "idiomas": [
            {"lingua": "Inglês", "nivel": "Avançado / Fluente"},
            {"lingua": "Espanhol", "nivel": "Intermediário"}
        ]
    }
    return render_template('curriculo.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)
