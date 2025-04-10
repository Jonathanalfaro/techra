let dataTableTickets;
let dataTableTicketsIsInitialized = false;
let dataTableUsuarios;
let dataTableUsuariosIsInitialized = false;
let dataTableEquipos;
let dataTableEquiposIsInitialized = false;
let dataTableRefacciones;
let dataTableRefaccionesIsInitialized = false;
let dataTableClientes;
let dataTableClientesIsInitialized = false;

let dataTable;
let dataTableIsInitialized = false;

const initDataTables = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }
    // await listDocuments()
    dataTable = $("table").DataTable({
        scrollCollapse: true,
        scrollY: 500,
        order: [[0, 'desc']],
        processing: true,
        layout: {
            topStart: {
                'pageLength': '',
                buttons: ['excel']
            }
        },
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
    dataTableIsInitialized = true;
}

const initDataTableTickets = async () => {
    if (dataTableTicketsIsInitialized) {
        dataTableTickets.destroy();
    }
    // await listDocuments()
    dataTableTickets = $("table").DataTable({
        scrollCollapse: true,
        scrollY: 500,
        order: [[0, 'desc']],
        processing: true,
        layout: {
            topStart: {
                'pageLength': '',
                buttons: ['excel']
            }
        },
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
        order: [[0, 'asc']],
        layout: {
            topStart: {
                buttons: ['excel']
            }
        },
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
        order: [[0, 'asc']],
        layout: {
            topStart: {
                buttons: ['excel']
            }
        },
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
const initDatatableRefacciones = async () => {
    if (dataTableRefaccionesIsInitialized) {
        dataTableRefacciones.destroy();
    }
    dataTableRefacciones = $("#refacciones").DataTable({
        scrollCollapse: true,
        order: [[0, 'desc']],
        scrollY: 500,
        layout: {
            topStart: {
                buttons: ['excel']
            }
        },
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
    dataTableRefaccionesIsInitialized = true;
}
const initDatatableClientes = async () => {
    if (dataTableClientesIsInitialized) {
        dataTableClientes.destroy();
    }
    dataTableClientes = $("#clientes").DataTable({
        scrollCollapse: true,
        order: [[0, 'desc']],
        scrollY: 500,
        layout: {
            topStart: {
                buttons: ['excel']
            }
        },
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
    dataTableClientesIsInitialized = true;
}


window.addEventListener('load', async () => {
    await initDataTables()
    $('.table-responsive').css({"visibility": "visible"});
    $('.spinner-border').css({"visibility": "hidden"});
})
