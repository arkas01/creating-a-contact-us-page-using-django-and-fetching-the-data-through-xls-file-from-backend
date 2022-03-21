from django.contrib import admin
from import_export.admin import ImportExportMixin
from home.models import Contact
# Register your models here.
class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'desc','date']

admin.site.register(Contact,TaskAdmin)