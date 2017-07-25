from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
import httplib2
import os
from django.conf import settings

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

try:
    import argparse
    #flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
#SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gestao de Recursos'


def get_credentials():
    """Gets valid user credentials from storage.
    Returns:
        Credentials, the obtained credential.
    """
    credential_dir = os.path.join(settings.PROJECT_ROOT, 'static')
    credential_path = os.path.join(credential_dir,
                                   'calendar-credential.json')
    client_secret_path= os.path.join(credential_dir,
                                   'client_secret.json')

    store = Storage(credential_path)
    credentials = store.get() #busca credencias no servidor
    if not credentials or credentials.invalid: 
        print('Issue with credentials' + credential_path)
    return credentials


if __name__ == '__main__':
    main()