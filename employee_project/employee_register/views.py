from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import EmployeeForm
# import sys

def create_employee(request):
    success_message = None
    
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                success_message = 'Form submitted successfully!'
                messages.success(request, success_message)
                return redirect('')
            except:
                pass
    else:
        form = EmployeeForm()
    # return render(request, 'create.html')
    return render(request, 'create.html', {'form':form})

# Search Blog
        
def retrieve_employee(request):
    employee = employee.objects.all()
    return render(request,'search.html',{'employee':employee} )