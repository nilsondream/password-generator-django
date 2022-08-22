from unicodedata import name
from django.shortcuts import render
import random
#from django.http import HttpResponse

def HomeView(request):
    #return HttpResponse('Hello')
    return render(request, 'home.html')

def AboutView(request):
    return render(request, 'about.html')

def PasswordView(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generate_password = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('*@%+^-$&~()'))
    
    if request.GET.get('special'):
        characters.extend(list('0123456789'))

    for char in range(length):
        generate_password += random.choice(characters)

    return render(request, 'password.html', {'password': generate_password})