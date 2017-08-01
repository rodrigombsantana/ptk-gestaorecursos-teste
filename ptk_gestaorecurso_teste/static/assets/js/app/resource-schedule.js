$(document).ready(function(){

  $('.datepicker').datepicker({
    autoclose: true
  });

  $('#schedule-btn').click(function(){
    $('#resource-schedule-modal').modal('hide');
    toastr.info('Recurso agendado com sucesso!','');
  });

});
