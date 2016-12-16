from django.contrib import admin

# Register your models here.
from .models import Nutricionista, Paciente, Ficha, Clasificacion, Alimento, Minuta

admin.site.register(Nutricionista)
admin.site.register(Paciente)
admin.site.register(Ficha)
admin.site.register(Clasificacion)
admin.site.register(Alimento)
admin.site.register(Minuta)