document.addEventListener("DOMContentLoaded", () => {
    const listaCurso = document.querySelector('#lista-cursos');
    let carritoArray = JSON.parse(localStorage.getItem('carrito')) || [];

    listaCurso.addEventListener('click', (e) => {
        e.preventDefault();

        if (e.target.classList.contains('productos')) {
            const card = e.target.parentElement.parentElement;
            leerDatos(card);
           
        }
    });

    function leerDatos(card) {
        const cursoSeleccionado = {
            imagen: card.querySelector('.card-img-top').img,
            nombre: card.querySelector('.card-title').h5,
            precio: card.querySelector('.total').span,
            cantidad: 1,
        };
        

        const existe = carritoArray.some((curso) => curso.nombre === cursoSeleccionado.nombre);
        if (existe) {
            carritoArray = carritoArray.map(curso => {
                if (curso.nombre === cursoSeleccionado.nombre) {
                    curso.cantidad++;
                }
                return curso;
            });
        } else {
            carritoArray = [...carritoArray, cursoSeleccionado];
        }

        sincronizarStorage();
    }

    function sincronizarStorage() {
        localStorage.setItem('carrito', JSON.stringify(carritoArray));
    }
});
