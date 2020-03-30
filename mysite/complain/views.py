from django.shortcuts import render
from .models import Complain

def display(request):
    return render(request, 'complain_display.html')

def register(request):
    return render(request, 'complain_register.html')

def save(request):
    if request.method == 'POST':
        complain = Complain()
        complain.student_name = request.POST.get('name')
        complain.title = request.POST.get('title')
        complain.description = request.POST.get('description')
        complain.save()
        if complain in Complain.objects.all():
            return render(request, 'complain_successful.html')
        else:
            return render(request, 'complain_unsuccessful.html')
    
# def success(request):
#     return render(request, 'complain_successful.html')

# def fail(request):
#     return render(request, 'complain_unsuccessful.html')
