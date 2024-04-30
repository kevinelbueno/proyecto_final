document.addEventListener("DOMContentLoaded", function() {
    const agregarCarritoButton = document.querySelector('.agregar-carrito');

    // Verificar si el botón de agregar al carrito existe en la página
    if (agregarCarritoButton) {
        // Agregar event listener al botón
        agregarCarritoButton.addEventListener('click', function() {
            // Lógica para agregar al carrito aquí
            console.log('Producto agregado al carrito');
        });
    }
});
