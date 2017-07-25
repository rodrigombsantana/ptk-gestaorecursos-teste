from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import usuario_acesso, recursos

#admin.site.register(Usuario, UserAdmin)
class usuario_acesso_adm (admin.ModelAdmin):
    list_display = ['user','escrita']#lista de campos mostrados na tela do admin
admin.site.register(usuario_acesso,usuario_acesso_adm) #registra model na tela do admin
class recursos_adm (admin.ModelAdmin):
    list_display = ['nome','nome_google','tipo','email_responsavel']#lista de campos mostrados na tela do admin
admin.site.register(recursos,recursos_adm) #registra model na tela do admin