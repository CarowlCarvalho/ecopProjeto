from django.contrib import admin

from .models import Enderecos

class EnderecosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'rua', 'n', 'bairro')


admin.site.register(Enderecos, EnderecosAdmin)


# Register your models here.
