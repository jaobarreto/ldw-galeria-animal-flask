from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
from config import config

app = Flask(__name__)
app.config.from_object(config['default'])
app.config.from_pyfile('config.py')

config['default'].init_app(app)

db = SQLAlchemy(app)


class Gatinho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    arquivo = db.Column(db.String(100), nullable=False)


@app.route('/')
def index():
    gatinhos = Gatinho.query.all()
    return render_template('index.html', gatinhos=gatinhos)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'arquivo' not in request.files:
            flash('Nenhum arquivo enviado')
            return redirect(request.url)

        arquivo = request.files['arquivo']

        if arquivo.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)

        if arquivo and allowed_file(arquivo.filename):
            filename = secure_filename(arquivo.filename)
            caminho = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            arquivo.save(caminho)

            novo_gatinho = Gatinho(
                titulo=request.form['titulo'],
                descricao=request.form['descricao'],
                arquivo=filename
            )
            db.session.add(novo_gatinho)
            db.session.commit()

            flash('Gatinho cadastrado com sucesso!')
            return redirect(url_for('index'))

    return render_template('upload.html')


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    gatinho = Gatinho.query.get_or_404(id)

    if request.method == 'POST':
        gatinho.titulo = request.form['titulo']
        gatinho.descricao = request.form['descricao']

        arquivo = request.files.get('arquivo')
        if arquivo and allowed_file(arquivo.filename):
            # Apagar o arquivo antigo
            caminho_antigo = os.path.join(app.config['UPLOAD_FOLDER'], gatinho.arquivo)
            if os.path.exists(caminho_antigo):
                os.remove(caminho_antigo)

            # Salvar novo arquivo
            filename = secure_filename(arquivo.filename)
            caminho_novo = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            arquivo.save(caminho_novo)
            gatinho.arquivo = filename

        db.session.commit()
        flash('Gatinho atualizado com sucesso!')
        return redirect(url_for('index'))

    return render_template('editar.html', gatinho=gatinho)


@app.route('/excluir/<int:id>')
def excluir(id):
    gatinho = Gatinho.query.get_or_404(id)

    # Apagar o arquivo da imagem
    caminho = os.path.join(app.config['UPLOAD_FOLDER'], gatinho.arquivo)
    if os.path.exists(caminho):
        os.remove(caminho)

    db.session.delete(gatinho)
    db.session.commit()
    flash('Gatinho excluído com sucesso!')
    return redirect(url_for('index'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=4000, debug=True)
