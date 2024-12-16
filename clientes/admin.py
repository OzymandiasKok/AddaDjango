from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'empresa')  # Campos que aparecerão na lista
    search_fields = ('nome', 'email')  # Campos para barra de pesquisa
    list_filter = ('empresa',)  #