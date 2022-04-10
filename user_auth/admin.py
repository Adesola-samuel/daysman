from django.contrib import admin
from .models import Biodata


class BiodataAdmin(admin.ModelAdmin):
    list_display = ('user', '_clas', 'gender','phn')

admin.site.register(Biodata, BiodataAdmin)
