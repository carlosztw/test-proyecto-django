/* BOTON ELIMINAR */

function confirmarEliminar(id){ 
    swal.fire({
        title: '¿Estás seguro?',
        text: "El producto será eliminado de la base de datos.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#4CAF50',
        cancelButtonColor: '#f44336' ,
        confirmButtonText: 'Sí',
        cancelButtonText: 'No',
        reverseButtons: true
    }).then((result) => {
        if (result.isConfirmed) {
        swal.fire({
            title: '¡Eliminado!',
            text: 'El producto ha sido eliminado de la base de datos.',
            icon: 'success',
            confirmButtonColor: '#4CAF50'
        }).then(function() {
            window.location.href = "/eliminarproducto/"+id+"/";
        })
        } else if (
        /* Read more about handling dismissals below */
        result.dismiss === Swal.DismissReason.cancel
        ) {
        swal.fire({
            title: 'Cancelado',
            text: 'El producto no ha sido eliminado.',
            icon: 'error',
            confirmButtonColor: '#4CAF50'
        })
        }
    })
}

