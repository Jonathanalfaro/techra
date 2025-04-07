let dataTableTickets;
let dataTableTicketsIsInitialized = false;

let dataTableUsuarios;
let dataTableUsuariosIsInitialized = false;


let dataTableEquipos;
let dataTableEquiposIsInitialized = false;

const initDataTableTickets = async () => {
    if (dataTableTicketsIsInitialized) {
        dataTableTickets.destroy();
    }
    // await listDocuments()
    dataTableTickets = $("#tickets").DataTable({
        scrollCollapse: true,
        scrollY: 500,
        processing: true,
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        }
    });
    $("#tickets").show()
    dataTableTicketsIsInitialized = true;
}

const initDatatableUsuarios = async () => {
    if (dataTableUsuariosIsInitialized) {
        dataTableUsuarios.destroy();
    }
    dataTableUsuarios = $("#usuarios").DataTable({
        scrollCollapse: true,
        scrollY: 500,
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        }
    });
    dataTableUsuariosIsInitialized = true;
}

const initDatatableEquipos = async () => {
    if (dataTableEquiposIsInitialized) {
        dataTableEquipos.destroy();
    }
    dataTableEquipos = $("#equipos").DataTable({
        scrollCollapse: true,
        scrollY: 500,
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        }
    });
    dataTableEquiposIsInitialized = true;
}

window.addEventListener('load', async () => {
    await initDataTableTickets()
    $('#div-tickets').css({"visibility":"visible"});
    $('#loading-tickets').css({"visibility":"hidden"});
    await initDatatableUsuarios()
    $('#div-usuarios').css({"visibility":"visible"});
    $('#loading-users').css({"visibility":"hidden"});
    await  initDatatableEquipos()
    $('#div-equipos').css({"visibility":"visible"});
    $('#loading-equipos').css({"visibility":"hidden"});
})
