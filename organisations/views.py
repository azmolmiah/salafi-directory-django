from django.shortcuts import render

def index(request):
    return render(request, 'organisations/organisations.html')

def organisation(request):
    return render(request, 'organisations/organisation.html')

def search(request):
    return render(request, 'organisations/search.html')