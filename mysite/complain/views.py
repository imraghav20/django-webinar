from django.shortcuts import render

def register(request):
    return render(request, 'complain_register.html')

def success(request):
    return render(request, 'complain_successful.html')

def fail(request):
    return render(request, 'complain_unsuccessful.html')
