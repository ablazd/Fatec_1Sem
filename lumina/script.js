{

}

{
    let slideIndex = 1;
    mostrarDiv(slideIndex);

    function mostrarDiv(novoIndice) {
        slideIndex = novoIndice
        let itens = document.getElementsByClassName(`slideItem`);
        let divAtual = document.getElementsByClassName(`divAtual`);
        let textos = document.getElementsByClassName(`texto`);
        let circuloAtivo = document.getElementsByClassName(`circulo`);
        for (let i = 0; i < itens.length; i++) {
            itens[i].style.display = `none`;
            textos[i].style.display = `none`;
            circuloAtivo[i].style.background = `none`;
        }
        for (let i = 0; i < divAtual.length; i++) {
            divAtual[i].className = divAtual[i].className.replace(` divAtiva`, ``);
        }
        itens[slideIndex - 1].style.display = `block`;
        divAtual[slideIndex - 1].className += ` divAtiva`;
        textos[slideIndex - 1].style.display = `flex`;
        circuloAtivo[slideIndex - 1].style.background = `#129E97`;
    }
}