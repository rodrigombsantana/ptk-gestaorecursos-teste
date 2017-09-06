"""ptk_gestaorecurso_teste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from ptk_gestaorecurso_teste.recursos import views,g_calendario #importar views a serem mostradas


urlpatterns = [
	url(r'^$', views.v_agendamento, name='home'),  #chamada direta do home, nao é string
	#url(r'^agendar/', views.v_agendamento, name='agendar'),
	#url(r'^google/', g_calendario.load, name='g_calendario'),
    #url(r'^', include('ptk_gestaorecurso_teste.recursos.urls', namespace='recursos')),
	#url(r'^resource-schedule/', name='resource-schedule'),
	url(r'^admin/', admin.site.urls),
	url(r'^login/', auth_views.login, {'template_name': 'login.html'}, name='login'),


]
