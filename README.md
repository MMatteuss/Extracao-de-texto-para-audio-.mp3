# Projeto de Extração de Texto para Áudio (MP3) com Flask

Este projeto tem como objetivo transformar textos digitados pelo usuário em arquivos de áudio MP3, utilizando a biblioteca **gTTS (Google Text-to-Speech)** para gerar a fala e **Flask** para construir a interface web. O usuário pode digitar um texto, selecionar um idioma e fazer o download do áudio gerado.

## Tecnologias Utilizadas

- **Python**: Backend para o gerenciamento da aplicação.
- **Flask**: Framework utilizado para criação do servidor web.
- **gTTS**: Biblioteca para conversão de texto em áudio.
- **HTML/CSS**: Para criação da interface do usuário.
- **JavaScript**: Para interatividade na página.

## Funcionalidades

- Conversão de textos digitados para áudio no formato MP3.
- Suporte para múltiplos idiomas: Português, Inglês, Francês, Espanhol.
- Interface simples e intuitiva para o usuário digitar o texto e escolher o idioma.
- O arquivo de áudio gerado é enviado para o usuário com um nome personalizável.

## Como Funciona

1. **Interface do Usuário**:
    - O usuário acessa a página web e é apresentado a um formulário simples.
    - Ele pode digitar o texto que deseja transformar em áudio.
    - Pode escolher o idioma da fala (Português, Inglês, Francês ou Espanhol).
    - O usuário também pode personalizar o nome do arquivo de áudio.

2. **Processamento**:
    - O texto digitado é enviado ao backend onde é processado pela API **gTTS**.
    - O áudio gerado é salvo como um arquivo MP3 e o usuário pode fazer o download.

## Como Rodar o Projeto

### Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado em sua máquina.

### Passo a Passo

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/seu-usuario/Extracao-de-texto-para-audio-mp3.git
    cd Extracao-de-texto-para-audio-mp3
    ```

2. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Execute o servidor Flask**:
    ```bash
    python app.py
    ```

4. Acesse a aplicação no navegador através do seguinte endereço:
    ```
    http://localhost:8080
    ```

## Estrutura do Projeto

O projeto possui os seguintes arquivos e pastas:

