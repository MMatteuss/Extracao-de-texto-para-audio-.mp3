from flask import Flask, render_template, request
from gtts import gTTS

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    texto = request.form['textos']
    nomeArquivo = request.form['nomeArquivo']
    lingua = request.form['idiomas']

    audio(textoHtml=texto, nomeArquivoHtml=nomeArquivo, linguaHtml=lingua)

    return render_template('home.html')


def audio(textoHtml, nomeArquivoHtml, linguaHtml):
    texto = textoHtml
    lingua = linguaHtml
    nomeAudio = nomeArquivoHtml+".mp3"

    audio = gTTS(text=texto, lang=lingua, slow=False)

    audio.save(nomeAudio)

if __name__ == '__main__':
    app.run(debug=True)
