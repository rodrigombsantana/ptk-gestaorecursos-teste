$(document).ready(function(){

  $("#login").click(function(e){
    e.preventDefault();
    var username = $("#username").val();
    var password = $("#password").val();
    if(username == 'rodrigo' && password == '123456') {
      window.location.href = 'resource-schedule.html';
    } else {
      toastr.error('Não foi possível concluir a autenticação.', 'Usuário ou Senha inválido')
    }
    return false;
  });

});
