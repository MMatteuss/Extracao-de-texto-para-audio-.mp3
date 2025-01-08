from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    texto = request.form['textos']
    nomeArquivo = request.form['nomeArquivo']
    lingua = request.form['idiomas']

    #region
    pasta = "audios"
    os.makedirs(pasta, exist_ok=True)

    caminhoAudio = audio(textoHtml=texto, nomeArquivoHtml=nomeArquivo, linguaHtml=lingua, pasta=pasta)
    return send_file(caminhoAudio, as_attachment=True)
    #endregion

def audio(textoHtml, nomeArquivoHtml, linguaHtml, pasta):
    texto = textoHtml
    lingua = linguaHtml
    nomeAudio = f"{nomeArquivoHtml}.mp3"

    #region
    caminhoAudio = os.path.join(pasta, nomeAudio)

    audio = gTTS(text=texto, lang=lingua, slow=False)
    audio.save(caminhoAudio)

    return caminhoAudio
    #endregion

if __name__ == '__main__':
    app.run(debug=True)
