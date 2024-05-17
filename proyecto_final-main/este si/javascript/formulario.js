$(document).ready(function() {
    $('#registrationForm').on('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting normally

        let nombreCompleto = $('#nombreCompleto').val().trim();
        let fechaNacimiento = $('#fechaNacimiento').val();
        let correo = $('#correo').val().trim();
        let telefono = $('#telefono').val().trim();
        let direccion = $('#direccion').val().trim();
        let codigoPostal = $('#codigoPostal').val().trim();
        let rut = $('#rut').val().trim();

        let errorMessages = '';

        if (nombreCompleto === '') {
            errorMessages += 'El nombre completo es obligatorio.<br>';
        }

        if (fechaNacimiento === '') {
            errorMessages += 'La fecha de nacimiento es obligatoria.<br>';
        }

        const correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!correoRegex.test(correo)) {
            errorMessages += 'El correo electrónico no es válido.<br>';
        }

        const telefonoRegex = /^\d{10}$/;
        if (!telefonoRegex.test(telefono)) {
            errorMessages += 'El número de teléfono debe tener 10 dígitos.<br>';
        }

        if (direccion === '') {
            errorMessages += 'La dirección es obligatoria.<br>';
        }

        const codigoPostalRegex = "\d{10}";
        if (!codigoPostalRegex.test(codigoPostal)) {
            errorMessages += 'El código postal debe tener 5 dígitos.<br>';
        }

        if (rut === '') {
            errorMessages += 'El RUT es obligatorio.<br>';
        }

        let $errorContainer = $('#errorMessages');
        let $successMessage = $('#successMessage'); // Nuevo elemento para el mensaje de éxito
        if (errorMessages !== '') {
            $errorContainer.html(errorMessages);
            $successMessage.hide(); // Ocultar el mensaje de éxito si hay errores
        } else {
            $errorContainer.html('');
            $successMessage.show().text('Enviado con éxito!'); // Mostrar mensaje de éxito
            setTimeout(function() {
                $successMessage.fadeOut(); // Ocultar mensaje de éxito después de unos segundos
            }, 3000);
            $('#registrationForm')[0].reset();
        }
    });

    $('#backButton').on('click', function() {
        window.location.href = 'contactospage.html';
    });
});
