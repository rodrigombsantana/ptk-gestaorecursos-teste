from django.shortcuts import render
from django.http import HttpResponse
from .models import agendamento
from .forms import frm_agendamento
import httplib2
# Create your views here.

def v_home (request):
	#return render(request, 'home.html', {'usuario' : 'Rodrigo'})
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('calendar', 'v3', http=http)
	return render(request, 'home.html')
	#return HttpResponse('teste 1')

def v_agendamento (request):
	#return render(request, 'agendar.html')
	context = {}
	if request.method == 'POST':
		form = frm_agendamento(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			#form.cleaned_data['data_agendamento']
			form.save()
			form = frm_agendamento()
	else:
		form = frm_agendamento()
	context['form'] = form
	template_name = 'agendar.html'

	return render(request, template_name, context)
	#return HttpResponse('teste 1')

