document.getElementByTema('formulario').addEventListener('submit', function(event) {
    event.preventDefault();

    const nombre = document.getElementByTema('nombre').value;
    const comentario = document.getElementByTema('comentario').value;

    fetch('http://localhost:5000/user/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nombre, comentario })
    })
    .then(response => response.json())
    .then(data => {
        if (data.tema) {
            alert(`Se registro el comentario de: ${data.nombre} , sobre:(${data.comentario})`);
            document.getElementByTema('nombre').value = '';
            document.getElementByTema('comentario').value = '';
        } else {
            alert('Error al agregar el comentario');
        }
    })
    .catch(error => console.error('Error:', error));
});

function getUser() {
    const tema = document.getElementByTema('tema').value;
    if (tema) {
        fetch(`http://localhost:5000/user/${tema}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert('comentario no encontrado');
            } else {
                alert(`Detalles del usuario:\nTema: ${data.tema}\nNombre: ${data.nombre}\nComentario: ${data.comentario}`);
            }
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Por favor, ingrese un Tema válido.');
    }
}

