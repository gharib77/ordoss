from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from demo.models.personne import Personne
@admin.register(Personne)

class PersonneAdmin(ImportExportModelAdmin):
    pass