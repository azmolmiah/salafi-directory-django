from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django_countries import countries
from django.core.mail import send_mail
from .models import Organisation


def index(request):
    queryset_list = Organisation.objects.order_by('-created')
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(name__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Country
    if 'country' in request.GET:
        country = request.GET['country']
        if country:
            queryset_list = queryset_list.filter(country__iexact=country)

    # Type
    if 'types' in request.GET:
        types = request.GET['types']
        if types:
            queryset_list = queryset_list.filter(types__iexact=types)

    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_organisations = paginator.get_page(page)
    context = {
        'organisations': paged_organisations,
        'countries': countries,
        'values': request.GET
    }
    return render(request, 'organisations/organisations.html', context)


def organisation(request, organisation_id):
    organisation = get_object_or_404(Organisation, pk=organisation_id)
    context = {
        'organisation': organisation
    }

    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    message = request.POST.get('message')
    orgemail = request.POST.get('organisation_email')

    # Send mail
    send_mail(
        f'{organisation.name} Inquiry',
        f'Name: {name},\nEmail: {email},\nPhone: {phone},\nMessage: {message}',
        'info@salafidirectory.co.uk',
        [organisation.email, 'azmol.miah.general@gmail.com'],
        fail_silently=False
    )
    return render(request, 'organisations/organisation.html', context)
