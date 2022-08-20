document.addEventListener('DOMContentLoaded', function(){
    activeMenu();
    removeClass();
    newQR();
});


let slideBurger = document.querySelector('.slide__burger');
slideBurger.remove();

const body = document.querySelector('body');
const filtro = document.querySelector('.containpage__filtro');
const filtroEnlaces = document.querySelector('.containpage__filtro-enlaces');
const contenedorQR = document.querySelector('.div__codigoqr')

function removeClass(){
    const pspin = document.querySelector('.p-spinmovies');
    const contenedor = document.querySelector('.contenido');
    if(pspin){
        if(window.innerWidth < 900){
            pspin.remove();
            contenedor.classList.remove('contenido');
            contenedor.classList.add('contenidoPx');
        } else {
            contenedor.classList.remove('contenidoPx')
        }
    }

    if(filtroEnlaces != null){
        if(window.innerWidth < 900){
            filtroEnlaces.remove();
            const btnFiltro = document.createElement('BUTTON');
            btnFiltro.classList.add('btnFiltro');
            btnFiltro.textContent = 'Filtro'
            filtro.appendChild(btnFiltro);
    
            btnFiltro.addEventListener('click', function(){
                filtro.appendChild(filtroEnlaces);
            });
        }
    }
}

function activeMenu(){
    let bars_menu = document.querySelector('.bars__menu');
    let valorClick = 0;
    bars_menu.addEventListener("click", function (e){
        valorClick+=1;
        let lineOne = document.querySelector(".line1__bars-menu");
        let lineTwo = document.querySelector(".line2__bars-menu");
        let lineThree = document.querySelector(".line3__bars-menu");

        lineOne.classList.toggle("activeline1__bars-menu");
        lineTwo.classList.toggle("activeline2__bars-menu");
        lineThree.classList.toggle("activeline3__bars-menu");
        
        if(valorClick === 1){
            slideBurger.classList.add('slide__burger')
            slideBurger.classList.remove('slide__burger-close');
            body.appendChild(slideBurger);
            body.classList.add('fijar-body');
        } else {
            slideBurger.classList.add('slide__burger-close');
            slideBurger.classList.remove('slide__burger');
            body.classList.remove('fijar-body')
            valorClick = 0;
        }
    });
}

//

function newQR(){
    new QRCode(contenedorQR, 'https://www.spinmovies.com/');
}