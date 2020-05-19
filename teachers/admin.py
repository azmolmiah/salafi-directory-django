from django.contrib import admin

from .models import Teacher

from django_admin_listfilter_dropdown.filters import DropdownFilter

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'type')
    list_filter = (('country', DropdownFilter),'type')
    search_fields = ('name',)

admin.site.register(Teacher, TeacherAdmin)
