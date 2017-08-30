from django.shortcuts import render
#from django.http import HttpResponse
from .models import agendamento, recursos
from .forms import frm_agendamento
from .g_calendario import get_credentials
import httplib2
from apiclient import discovery
from datetime import datetime
#from .apps import myconverter
import json
from django.core.serializers.json import DjangoJSONEncoder
#from oauth2client.contrib import django_util
#from oauth2client import client
#from oauth2client import tools
#from oauth2client.file import Storage

# Create your views here.

def v_home (request):
	#return render(request, 'home.html', {'usuario' : 'Rodrigo'})
	#credentials = get_credentials()
	#http = credentials.authorize(httplib2.Http())
	#service = discovery.build('calendar', 'v3', http=http)
	#page_token = None
	#while True:
	#	calendar_list = service.calendarList().list(pageToken=page_token).execute()
	#	for calendar_list_entry in calendar_list['items']:
	#		print (calendar_list_entry['summary'])
	#	page_token = calendar_list.get('nextPageToken')
	#	if not page_token:
	#		break
	recurso = recursos.objects.all()
	context = {
		'recursos' : recurso
	}

	return render(request, 'resource-schedule.html', context)
	#return HttpResponse('teste 1')

#@oauth_required
def v_agendamento (request):
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('calendar', 'v3', http=http)
	recurso = recursos.objects.all()
	context = {
		'recursos' : recurso
	}
	if request.method == 'POST':
		print(request.POST)
		form = frm_agendamento(request.POST)
		recurso_selecionado = request.POST.get('recurso-selecionado')
		if form.is_valid() and recurso_selecionado is not None:
			context['is_valid'] = True
			datai_combinada = datetime.combine(form.cleaned_data['data_agendamento'],form.cleaned_data['horario_inicio'])
			dataf_combinada = datetime.combine(form.cleaned_data['data_agendamento'],form.cleaned_data['horario_fim'])
			event = {
			      'summary': 'Rodrigo Teste',
			      'description': form.cleaned_data['motivo'] ,
			      'start': {
			        'dateTime': datai_combinada,
			        #'dateTime': '2017-07-27T09:00:00',
			        'timeZone': 'America/Sao_Paulo',
			      },
			      'end': {
			        'dateTime': dataf_combinada,
			        #'dateTime': '2017-07-27T10:00:00',
			        'timeZone': 'America/Sao_Paulo',
			      }
			    }
			json_s=json.dumps(event, cls=DjangoJSONEncoder)  #serializa para JSON
			event_final=json.loads(json_s) #carrega JSON
			event = service.events().insert(calendarId=recurso_selecionado, body=event_final).execute() #cria evento no calendario
			db_save=form.save(commit=False)  #salva dados do formulario mao nao faz commit
			db_save.google_link = event.get('id')
			db_save.save() # commit no banco de dados
			form = frm_agendamento()
		else:
			context['is_error'] = True
			#print(event.get('id'))
			#print(v_deleta_agendamento(event.get('id')))
			#print(v_atualiza_agendamento(event.get('id'),event1))
	else:
		form = frm_agendamento()
	context['form'] = form
	template_name = 'resource-schedule.html'

	return render(request, template_name, context)

def v_deleta_agendamento (eventId):
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('calendar', 'v3', http=http)
	service.events().delete(calendarId='sjc.pantokrator.ti@gmail.com', eventId=eventId).execute()#deleta do google
	agendamento.objects.filter(google_link=eventId).delete()#deleta do banco
	return 'deletado'


def v_atualiza_agendamento (eventId, event):
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('calendar', 'v3', http=http)
	#updated_event = service.events().update(calendarId='sjc.pantokrator.ti@gmail.com', eventId=eventId, body=event).execute()
	agendamento.objects.filter(google_link=eventId).update(data_agendamento=datetime.strftime(event['start']['dateTime'],"%Y-%m-%d"),
														   horario_inicio=datetime.strftime(event['start']['dateTime'],"%H:%M"),
														   horario_fim=datetime.strftime(event['end']['dateTime'],"%H:%M"),
														   motivo=event['description'])
	return 'atualizado'
