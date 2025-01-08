var btn = document.getElementById("btn").disabled = true;
var number = 0

document.getElementById("textos").addEventListener("input", function(event){
    var textos = document.getElementById("textos").value;

    if (textos !== null  && textos !== '') {
      number= number + 1;
    } else {
      number=0
    }
});

document.getElementById("nomeArquivo").addEventListener("input", function(event){
    var nomeArquivo = document.getElementById("nomeArquivo").value;

    if (nomeArquivo !== null  && nomeArquivo !== '') {
        number= number + 1;
    } else {
      number=0
    }
});

document.addEventListener("input", function event(){
    if (number == 2){
        document.getElementById("btn").disabled = false;
    }
})