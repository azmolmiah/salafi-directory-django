from django.contrib import admin
from django.contrib.auth.models import User
from django_admin_listfilter_dropdown.filters import DropdownFilter
from .models import Organisation

class OrganisationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(account=request.user)

    
    list_display = ('name', 'city', 'country')
    list_filter = (('city', DropdownFilter), 
                   ('country', DropdownFilter),)
    search_fields = ('name', 'country', 'address', 'zipcode')
    list_per_page = 10


admin.site.register(Organisation, OrganisationAdmin)
