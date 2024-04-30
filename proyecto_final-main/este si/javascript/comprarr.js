document.addEventListener("DOMContentLoaded", function() {
    const agregarCarritoButtons = document.querySelectorAll('.agregar-carrito');
    const cantidadCarrito = document.getElementById('cantidad-carrito');

    // Verificar si hay elementos guardados en el carrito en el almacenamiento local
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    // Actualizar la cantidad en el enlace del carrito
    cantidadCarrito.textContent = carrito.length;

    // Agregar productos al carrito
    agregarCarritoButtons.forEach(button => {
        button.addEventListener('click', agregarAlCarrito);
    });

    function agregarAlCarrito(event) {
        const button = event.target;
        const producto = button.parentElement;
        const nombre = producto.querySelector('h3').innerText;
        const precio = parseInt(producto.querySelector('.precio').innerText.slice(1)); // Obtener el precio del producto

        // Crear objeto de producto con nombre y precio
        const productoAgregar = {
            nombre: nombre,
            precio: precio
        };

        // Agregar producto al carrito
        carrito.push(productoAgregar);
        localStorage.setItem('carrito', JSON.stringify(carrito));

        // Actualizar cantidad en el enlace del carrito
        cantidadCarrito.textContent = carrito.length;
    }
});


    // Mostrar los elementos del carrito
    mostrarCarrito();

    function mostrarCarrito() {
        carritoLista.innerHTML = '';
        totalPrecio.textContent = '$0';

        carrito.forEach(item => {
            const carritoItem = document.createElement('div');
            carritoItem.classList.add('carrito-item');
            carritoItem.innerHTML = `
                <img src="imagen1.jpg" alt="${item.nombre}">
                <span>${item.nombre}</span>
                <span>$${item.precio}</span>
            `;
            carritoLista.appendChild(carritoItem);
        });

        // Calcular y mostrar el total
        calcularTotal();
    }

    // Calcular el total del carrito
    function calcularTotal() {
        let total = 0;
        carrito.forEach(item => {
            total += parseInt(item.precio);
        });
        totalPrecio.textContent = `$${total}`;
    }

    // Vaciar el carrito
    vaciarCarritoButton.addEventListener('click', () => {
        carrito = [];
        localStorage.setItem('carrito', JSON.stringify(carrito));
        mostrarCarrito();
    });

    // Pagar
    pagarButton.addEventListener('click', () => {
        alert('¡Gracias por tu compra!');
        carrito = [];
        localStorage.setItem('carrito', JSON.stringify(carrito));
        mostrarCarrito();
    });

