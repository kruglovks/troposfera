"""docs"""
from django.shortcuts import render

def index(request):
    """docstring"""
    animals = ['Zebra', 'Cat', 'Dog']
    return render(request, 'blog/index.html', context={'animals': animals})
