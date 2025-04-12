pip install flask

___________________________________________

meu_projeto/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── contato.html
└── static/
    ├── css/
    └── js/

___________________________________________

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        mensagem = request.form['mensagem']
        return f"<h1>Obrigado, {nome}! Recebemos sua mensagem.</h1>"
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)


___________________________________________

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <h1>Minha Aplicação Flask</h1>
        <nav>
            <a href="{{ url_for('index') }}">Início</a>
            <a href="{{ url_for('contato') }}">Contato</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>

___________________________________________

{% extends 'base.html' %}
{% block content %}
<h2>Página Inicial</h2>
<p>Bem-vindo à minha aplicação Flask!</p>
{% endblock %}

___________________________________________

{% extends 'base.html' %}
{% block content %}
<h2>Contato</h2>
<form method="post">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome" required>
    <label for="mensagem">Mensagem:</label>
    <textarea id="mensagem" name="mensagem" required></textarea>
    <button type="submit">Enviar</button>
</form>
{% endblock %}

___________________________________________

python app.py
