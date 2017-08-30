$(document).ready(function(){

  var resourceScheduleUrlTemplate = "https://calendar.google.com/calendar/embed?src=:schedule-source:&ctz=America/Sao_Paulo";

  $('.datepicker').datepicker({
    autoclose: true
  });

  $('#schedule-btn').click(function(){
    //$('#resource-schedule-modal').modal('hide');
    //toastr.info('Recurso agendado com sucesso!','');
  });

  $( "#resource-schedule-modal" ).on('shown.bs.modal', function() {
      $("[name='horario_inicio']").val("12:00");
      $("[name='horario_fim']").val("13:00");
      $("[name='data_agendamento']").datepicker("update", new Date());
  });

  $('#resource-schedule-modal').on('hidden.bs.modal', function () {
    $('#schedule-form')[0].reset();
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
    $('#resource').val(selectedResourceCalendar);
  });

});
