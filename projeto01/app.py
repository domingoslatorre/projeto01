from flask import Flask, request

app = Flask(__name__)

# / index
@app.route('/')
def index():
    return '<h1>Olá mundo</h1>'


# /contato
@app.route('/contato')
def contato():
    return """
    <h1>Contato</h1>
    <form action="/submicao_form" method="post">
        <label>E-mail</label>
        <br>
        <input type="email" name="email" />
        <br>
        <label>Mensagem</label>
        <br>
        <textarea name="mensagem"></textarea>
        <br>
        <button type="submit">Enviar</button>
    </form>
    """

@app.route('/submicao_form', methods=['POST'])
def submicao_form():
    email = request.form['email']
    mensagem = request.form['mensagem']

    # enviar para o admin

    # salvar no banco

    return f"""
        {email}
        {mensagem}    
    """


# poetry run O QUE?
# poetry run python3 arquivo.py
# poetry run flask --app projeto01/app.py run
# flask --app projeto01/app.py run

