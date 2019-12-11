function confirmarEliminacion(id) {
    Swal.fire({
        title: '¿Estás seguro?',
        text:"No podras volver atrás",
        icon:'warning', 
        showCancelButton: true,
        confirmButtonColor:'#3085d6', 
        cancelButtonColor:'#d33',
        confirmButtonText:'Si, Eliminar', 
        cancelButtonText:'Cancelar'
        }).then((result) => {
        if(result.value) {
            window.location.href = "/eliminar-flor/"+id+"/";
        }
    })
}