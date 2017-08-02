$(document).ready(function(){

  var resourceScheduleUrlTemplate = "https://calendar.google.com/calendar/embed?src=:schedule-source:&ctz=America/Sao_Paulo";

  $('.datepicker').datepicker({
    autoclose: true
  });

  $('#schedule-btn').click(function(){
    $('#resource-schedule-modal').modal('hide');
    toastr.info('Recurso agendado com sucesso!','');
  });

  var buildCalendarUrl = function(calendarSource) {
    return resourceScheduleUrlTemplate.replace(':schedule-source:', calendarSource);
  }

  $('#resource-calendar').change(function(){
    if(!$(this).val()) {
      $('.calendar-box').hide();
    }
    var selectedResourceCalendar = $(this).val();
    var calendarUrl = buildCalendarUrl(selectedResourceCalendar);
    $('#calendar-frame').attr('src', calendarUrl);
    $('.calendar-box').show();
  });

});
