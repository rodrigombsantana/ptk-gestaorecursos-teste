from django.apps import AppConfig
from django.http import HttpResponse
from .g_calendario import get_credentials
import httplib2
from apiclient import discovery
from datetime import datetime,date

class RecursosConfig(AppConfig):
    name = 'recursos'

