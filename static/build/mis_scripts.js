
function init_datatables() {    

    if (typeof($.fn.DataTable) === 'undefined') {
        return;
    }

    console.log('init_datatables_mis_scripts');

        //Función de DataTable para establecer sus parámetros
        $("#dataTables").DataTable({
          dom: "Blfrtip",
          buttons: [{
                extend: "copy",
                className: "btn-primary",
                text: "Copiar"
            }, {
                extend: "csv",
                className: "btn-success",
                text: "Excel"
            }, {
                extend: "excel",
                className: "btn-sm",
                text: "Excel"
            }, {
                extend: "pdf",
                className: "btn-sm",
                text: "PDF"
            }, {
                extend: "print",
                className: "btn-primary",
                text: "Imprimir"
            }],
                //Cambiar el idioma, también se puede hacer con un json
                language: {
                            
                    "sProcessing":     "Procesando...",
                    "sLengthMenu":     "Mostrar _MENU_ registros",
                    "sZeroRecords":    "No se encontraron resultados",
                    "sEmptyTable":     "Ningún dato disponible en esta tabla",
                    "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
                    "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
                    "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
                    "sInfoPostFix":    "",
                    "sSearch":         "Buscar:",
                    "sUrl":            "",
                    "sInfoThousands":  ",",
                    "sLoadingRecords": "Cargando...",
                    "lengthChange": false,
                    "oPaginate": {
                        "sFirst":    "Primero",
                        "sLast":     "Último",
                        "sNext":     "Siguiente",
                        "sPrevious": "Anterior"
                    },
                    "oAria": {
                        "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
                        "sSortDescending": ": Activar para ordenar la columna de manera descendente"
                    }
                },
                paging: true,
                pagingType: "full_numbers",
                //responsive: true // No permitir que la tabla resultante sea responsive
                //"ordering": false // Deshabilitar las opciones de filtros en las columnas.
                "order": [[ 0, "desc" ]] // Indicar que se desea ordenar descendentemente la columna 0
            });
         
            // // Crear una variable de tipo dataTables, es decir del DIV de la tabla para poderla manipular.
            var table = $("#dataTables").DataTable();
         
            // // Aplicar las búsquedas por cada columna.
            table.columns().every( function () {
                var that = this;
                
                //En el tfooter se crearon los campos con th, se aplicada cada filtro a cada campo según su columna.
                $( 'input', this.footer() ).on( 'keyup change', function () {
                    if ( that.search() !== this.value ) {
                        that
                            .search( this.value )
                            .draw();
                    }
                } );
            });
    
};




function init_select2() {   

    console.log('init_select2_mis_scripts');

    // Campo Select2, para mostrar combobox
    $("#select2").select2({
        theme: "bootstrap",
        placeholder: " ---------Seleccionar---------",
        allowClear: true,
        width: '75%',
        containerCssClass: ':all:'
    });




    $("#select2_1").select2({
        theme: "bootstrap",
        placeholder: " ---------Seleccionar---------",
        allowClear: true,
        width: '75%',
        containerCssClass: ':all:'
    });



    $("#select2_2").select2({
        theme: "bootstrap",
        placeholder: " ---------Seleccionar---------",
        allowClear: true,
        width: '75%',
        containerCssClass: ':all:'
    });

    $("#select2_3").select2({
        theme: "bootstrap",
        placeholder: " ---------Seleccionar---------",
        allowClear: true,
        width: '75%',
        containerCssClass: ':all:'
    });
    
    // Campo Select2, para mostrar combobox multiple
    $("#multiSelect2").select2({
        theme: "bootstrap",
        maximumSelectionLength: 3,
        allowClear: true,
        width: '75%',
        tags: true,
        containerCssClass: ':all:'
    });   
};



function init_datapicker() { 
     
    if (typeof($.fn.datetimepicker) === 'undefined') {
        return;
    }

    console.log('init_datapicker_mis_scripts');

    // Calendario para fechas

    $('.myDatepicker').datetimepicker({
        format: 'DD/MM/YYYY',
        locale:'es'
    });
    
    

    $('.myDatepicker1').datetimepicker({
        format: 'DD/MM/YYYY',
        locale:'es'
    });


    $('.myDatepicker2').datetimepicker({
        format: 'DD/MM/YYYY',
        locale:'es'
    });
    
    $('.myDatepickerConsulta1').datetimepicker({
        format: 'YYYY-MM-DD',
        locale:'es'
    });

    $('.myDatepickerConsulta2').datetimepicker({
        format: 'YYYY-MM-DD',
        locale:'es'
    });

    $('.myDateTimepicker').datetimepicker({
        format: 'DD/MM/YYYY H:mm',
        //use24hours: true
        locale:'es',
        stepping: 15,
    });  
    
    $('.myDateTimepicker2').datetimepicker({
        format: 'DD/MM/YYYY H:mm',
        //use24hours: true
        locale:'es',
        stepping: 15,
    }); 
};



function init_Switchery() { 

    console.log('init_Switchery_mis_scripts');
    // Switchery
        if ($(".switch1")[0]) {
            var elems = Array.prototype.slice.call(document.querySelectorAll('.switch1'));
            elems.forEach(function(html) {
                var switchery = new Switchery(html, {
                    size: 'small',
                    //color: '#BBB7B7',
                    color: 'red',
                    //secondaryColor: '#26B99A',
                    //jackColor: '#26B99A',
                    //jackSecondaryColor: '#26B99A'
                });
            });
        }
};

function init_timepicker() { 
    $('#timepicker1').timepicker({ 
        timeFormat: 'H:mm:ss',
        showSeconds: true,
        showMeridian: false,
        defaultTime: false
    });
};







