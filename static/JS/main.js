document.getElementById("btn").disabled = true;
var numberEnviar = 0

// Botão enviar
document.getElementById("textos").addEventListener("input", function(event){
    var textos = document.getElementById("textos").value;

    if (textos !== null  && textos !== '') {
      numberEnviar= numberEnviar + 1;
    } else {
      numberEnviar=0
    }
});

document.getElementById("nomeArquivo").addEventListener("input", function(event){
    var nomeArquivo = document.getElementById("nomeArquivo").value;

    if (nomeArquivo !== null  && nomeArquivo !== '') {
        numberEnviar= numberEnviar + 1;
    } else {
      numberEnviar=0
    }
});

document.addEventListener("input", function event(){
    if (numberEnviar == 2){
        document.getElementById("btn").disabled = false;
    }
})



// Prevenção de envio sem texto
const form = document.querySelector("form");
const textarea = document.getElementById("textos");

form.addEventListener("submit", function (e) {
    if (!textarea.value.trim()) {
        e.preventDefault();
        alert("Por favor, insira um texto antes de enviar.");
    }
});