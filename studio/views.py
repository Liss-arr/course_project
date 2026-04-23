from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def studios(request):
    return render(request, 'studios.html')

def equipment(request):
    return render(request, 'equipment.html')

def services(request):
    return render(request, 'services.html')