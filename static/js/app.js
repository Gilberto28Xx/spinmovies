document.addEventListener("DOMContentLoaded",(function(){activeMenu(),removeClass(),newQR()}));let slideBurger=document.querySelector(".slide__burger");slideBurger.remove();const body=document.querySelector("body"),filtro=document.querySelector(".containpage__filtro"),filtroEnlaces=document.querySelector(".containpage__filtro-enlaces"),contenedorQR=document.querySelector(".div__codigoqr");function removeClass(){const e=document.querySelector(".p-spinmovies"),t=document.querySelector(".contenido");if(e&&(window.innerWidth<900?(e.remove(),t.classList.remove("contenido"),t.classList.add("contenidoPx")):t.classList.remove("contenidoPx")),null!=filtroEnlaces&&window.innerWidth<900){filtroEnlaces.remove();const e=document.createElement("BUTTON");e.classList.add("btnFiltro"),e.textContent="Filtro",filtro.appendChild(e),e.addEventListener("click",(function(){filtro.appendChild(filtroEnlaces)}))}}function activeMenu(){let e=document.querySelector(".bars__menu"),t=0;e.addEventListener("click",(function(e){t+=1;let n=document.querySelector(".line1__bars-menu"),o=document.querySelector(".line2__bars-menu"),r=document.querySelector(".line3__bars-menu");n.classList.toggle("activeline1__bars-menu"),o.classList.toggle("activeline2__bars-menu"),r.classList.toggle("activeline3__bars-menu"),1===t?(slideBurger.classList.add("slide__burger"),slideBurger.classList.remove("slide__burger-close"),body.appendChild(slideBurger),body.classList.add("fijar-body")):(slideBurger.classList.add("slide__burger-close"),slideBurger.classList.remove("slide__burger"),body.classList.remove("fijar-body"),t=0)}))}function newQR(){new QRCode(contenedorQR,"https://www.spinmovies.com/")}