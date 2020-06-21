from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.conf import settings


import stripe
stripe.api_key = settings.STRIPE_API_KEY

def index(request):
  return render(request, 'donations/donations.html')

def charge(request):
  if request.method == 'POST':
    print('Data:', request.POST)
    amount = int(request.POST['amount'])

    customer = stripe.Customer.create(
      email=request.POST['email'],
      name=request.POST['name'],
      source=request.POST['stripeToken'],
    )
    charge = stripe.Charge.create(
      customer=customer,
      amount=amount * 100,
      currency='gbp',
      description='Donation'
    )
  return redirect('success')

def success(request):
  return render(request, 'donations/success.html')
