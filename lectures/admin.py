from django.contrib import admin
from django.contrib.auth.models import User
from .models import Lecture

class LectureAdmin(admin.ModelAdmin):
  def get_queryset(self, request):
    qs = super().get_queryset(request)
    if request.user.is_superuser:
      return qs
    return qs.filter(author=request.user)

  list_display = ('title', 'teacher', 'organisation', 'is_online')
  list_filter = ('teacher',)
  search_fields = ('title', 'teacher__name', 'organisation__name',)
  list_per_page = 25

admin.site.register(Lecture, LectureAdmin)
