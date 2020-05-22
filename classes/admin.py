from django.contrib import admin

from .models import Class

class ClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'organisation', 'is_online')
    list_filter = ('teacher',)
    search_fields = ('title', 'teacher__name', 'organisation__name',)
    list_per_page = 25


admin.site.register(Class, ClassAdmin)
