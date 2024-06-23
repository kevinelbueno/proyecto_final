document.addEventListener('DOMContentLoaded', function() {
    fetch('../../menu/')
        .then(response => response.text())
        .then(data => {
            document.getElementById('menu-container').innerHTML = data;
        });
});
