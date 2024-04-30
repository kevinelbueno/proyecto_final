document.addEventListener("DOMContentLoaded", function() {
    const carritoLista = document.querySelector('.carrito-lista');
    const totalPrecio = document.querySelector('.total-precio');
    const vaciarCarritoButton = document.querySelector('.vaciar-carrito');
    const pagarButton = document.querySelector('.pagar');

    // Obtener productos del almacenamiento local
    let productosCarrito = JSON.parse(localStorage.getItem('carrito')) || [];

    // Mostrar productos en el carrito
    mostrarProductosCarrito();

    function mostrarProductosCarrito() {
        carritoLista.innerHTML = '';
        totalPrecio.textContent = '$0';

        if (productosCarrito.length === 0) {
            carritoLista.innerHTML = '<p>El carrito está vacío</p>';
            return;
        }

        let total = 0;
        productosCarrito.forEach(producto => {
            const productoItem = document.createElement('div');
            productoItem.classList.add('producto-carrito');
            productoItem.innerHTML = `
                <span>${producto.nombre}</span>
                <span>$${producto.precio}</span>
            `;
            carritoLista.appendChild(productoItem);

            total += producto.precio;
        });

        totalPrecio.textContent = `$${total}`;
    }

    // Vaciar el carrito
    vaciarCarritoButton.addEventListener('click', () => {
        productosCarrito = [];
        localStorage.setItem('carrito', JSON.stringify(productosCarrito));
        mostrarProductosCarrito();
    });

    // Pagar
    pagarButton.addEventListener('click', () => {
        alert('¡Gracias por tu compra!');
        productosCarrito = [];
        localStorage.setItem('carrito', JSON.stringify(productosCarrito));
        mostrarProductosCarrito();
    });
});
