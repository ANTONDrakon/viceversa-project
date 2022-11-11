
from django.shortcuts import render



def index(request):    
    return render(request, 'index.html')


def reverse(request):    
    return render(request, 'reverse.html')

