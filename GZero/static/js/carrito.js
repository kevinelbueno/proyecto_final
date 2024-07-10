document.addEventListener("DOMContentLoaded", () => {
    const carritoLista = document.querySelector('.carrito-lista');
    const totalPrecio = document.querySelector('.total-precio');
    const vaciarCarritoBtn = document.querySelector('.vaciar-carrito');
    const pagarBtn = document.querySelector('.pagar');

    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    function renderCarrito() {
        carritoLista.innerHTML = '';
        let total = 0;

        carrito.forEach((producto, carrrito) => {
            const div = document.createElement('div');
            div.classList.add('carrito-item');
            div.innerHTML = `
                <div class="row">
                    <div class="col-md-2">
                        <img src="${producto.imagen}" class="img-fluid">
                    </div>
                    <div class="col-md-3">
                        <p>${producto.nombre}</p>
                    </div>
                    <div class="col-md-2">
                        <p>${producto.precio}</p>
                    </div>
                    <div class="col-md-2">
                        <p>${producto.cantidad}</p>
                    </div>
                    <div class="col-md-3">
                        <button class="btn btn-danger btn-sm eliminar-producto" data-index="${index}">Eliminar</button>
                    </div>
                </div>
            `;
            carritoLista.appendChild(div);
            total += producto.precio * producto.cantidad;
        });

        totalPrecio.textContent = `$${total.toFixed(2)}`;
    }

    function vaciarCarrito() {
        carrito = [];
        sincronizarStorage();
        renderCarrito();
    }

    function pagar() {
        if (carrito.length === 0) {
            alert('El carrito está vacío');
            return;
        }
        alert('Compra realizada con éxito');
        vaciarCarrito();
    }

    function eliminarProducto() {
        carrito.splice(index, 1);
        sincronizarStorage();
        renderCarrito();
    }

    function sincronizarStorage() {
        localStorage.setItem('carrito', JSON.stringify(carrito));
    }

    carritoLista.addEventListener('click', (e) => {
        if (e.target.classList.contains('eliminar-producto')) {
            const index = e.target.dataset.index;
            eliminarProducto(index);
        }
    });

    vaciarCarritoBtn.addEventListener('click', vaciarCarrito);
    pagarBtn.addEventListener('click', pagar);

    renderCarrito();
});
