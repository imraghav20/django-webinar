from django.shortcuts import render

def register(request):
    return render(request, 'complain_register.html')
