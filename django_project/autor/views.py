from django.shortcuts import render

# Create your views here.
def showautor(request):
    return render(request,"autor/autor.html")