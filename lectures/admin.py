from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.contrib.auth.models import User
from .models import Lecture

class LectureChangeList(ChangeList):

    def __init__(self, request, model, list_display, list_display_links, list_filter, date_hierarchy, search_fields, list_select_related, list_per_page, list_max_show_all, list_editable, model_admin, sortable_by):

        super(LectureChangeList, self).__init__(request, model,
            list_display, list_display_links, list_filter,
            date_hierarchy, search_fields, list_select_related,
            list_per_page, list_max_show_all, list_editable, 
            model_admin, sortable_by)

class LectureAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(account=request.user)

    def get_changelist(self, request, **kwargs):
        self.list_display = ('title', 'date_And_Time', 'organisation', 'is_online')
        self.list_filter = ('date_And_Time',)
        self.search_fields = ('title',  'organisation__name',)
        self.list_per_page = 25
        return LectureChangeList

    def get_changelist_form(self, request, **kwargs):
        return Lecture

admin.site.register(Lecture, LectureAdmin)
