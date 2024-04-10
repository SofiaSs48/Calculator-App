from django.shortcuts import render, redirect
from .forms import NumberForm
#import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

def index(request):
  return render(request, 'python/index.html')

def calculator(request):
 form = NumberForm()  # Create an instance of the form
 return render(request, 'python/calculator.html', {'form': form})

def calculate_average(request):
 numbers = request.session.get('numbers', [])
 if request.method == 'POST':
  form = NumberForm(request.POST)
  if form.is_valid():
   number = form.cleaned_data['number']
   numbers.append(number)
   request.session['numbers'] = numbers  # Store numbers in session
   if len(numbers) >= 5:  # Check if 5 numbers have been entered
    total = sum(numbers)
    average = total / len(numbers)
    del request.session['numbers']  # Reset the stored numbers
    return render(request, 'python/index.html', {'average': average, 'numbers': numbers, 'form': NumberForm()})

  else:
   form = NumberForm()
 return render(request, 'python/index.html', {'form': form, 'numbers': numbers})

def cat_images(request):
  api_key = 'live_sZEaDfkZrElrlKQjHK5U7sTGpbg2PCKUSrS3vESPcILYLrMpJiNLe2egsZGo47VR'
  api_url = 'https://api.thecatapi.com/v1/images/search'
  response = requests.get(api_url, params={'api_key': api_key})
  cat_images = response.json()
# Extracting URLs from the response
  cat_urls = [cat['url'] for cat in cat_images]
# Passing the URLs to the template
  context = {'cat_urls': cat_urls}
  return render(request, 'python/cats.html', context)