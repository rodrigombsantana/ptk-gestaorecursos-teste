$(document).ready(function(){

  var resourceScheduleUrlTemplate = "https://calendar.google.com/calendar/embed?src=:schedule-source:&ctz=America/Sao_Paulo";

  $('.datepicker').datepicker({
    autoclose: true
  });

  $('#schedule-btn').click(function(){
    $('#resource-schedule-modal').modal('hide');
    toastr.info('Recurso agendado com sucesso!','');
  });

  $('#resource-calendar').change(function(){
    if(!$(this).val()) {
      $('.calendar-box').hide();
    }
    var selectedResourceCalendar = $(this).val();
    var calendarUrl = resourceScheduleUrlTemplate.replace(':schedule-source:', selectedResourceCalendar);
    $('#calendar-frame').attr('src', calendarUrl);
    $('.calendar-box').show();
  });

});
