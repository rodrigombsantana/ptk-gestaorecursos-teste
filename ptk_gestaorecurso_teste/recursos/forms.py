from django.db import models
from django.forms import ModelForm
from .models import agendamento
#import datetime
#class frm_agendamento(forms.ModelForm):
#
#    data_agendamento = forms.DateField(label="Data",initial=datetime.date.today)
#    horario_inicio = forms.TimeField(label="Inicio",initial=datetime.datetime.now().strftime('%H:%M'))
#    horario_fim = forms.TimeField(label="Fim", initial=datetime.datetime.now().strftime('%H:%M'))
#    
#    motivo = forms.CharField(
#        label='Motivo', widget=forms.Textarea
#    )

class frm_agendamento(ModelForm):  #formulario baseado em modelo
    class Meta:
        model = agendamento
        exclude = ('criado_em',) #campo que nao sera usado no formulario
