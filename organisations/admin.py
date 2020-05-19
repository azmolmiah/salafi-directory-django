from django.contrib import admin

from .models import Organisation

from django_admin_listfilter_dropdown.filters import DropdownFilter


class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = (('city', DropdownFilter),('country', DropdownFilter),)
    search_fields = ('name','country', 'address', 'zipcode')
    list_per_page = 10

admin.site.register(Organisation, OrganisationAdmin)
