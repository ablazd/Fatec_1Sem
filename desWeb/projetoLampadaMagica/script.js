let lampada=document.getElementById("lampada");

document.getElementById("titulo").style.color="red";

function ligar(){
    lampada.src="luzLigada.gif";
}

function desligar(){
    lampada.setAttribute("src", "luzDesligada.gif");
}

function sumir(){
    lampada.style.display = "none";
    //lampada.hidden = true;
}

function aparecer(){
    lampada.style.display = "inline";
    //lampada.hidden = false;
}

function alternar(){
    if (lampada.getAttribute("src") == "luzLigada.gif")
    {
    desligar();}

    else if(lampada.getAttribute("src") == "luzDesligada.gif")
    {
    ligar();}
}

function piscar(){
    alternar()
}
setInterval(piscar, 500);

