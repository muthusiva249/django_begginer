from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EmployeeForm
from .models import Employee
# import sys

def create_employee(request):
    success_message = None
    
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                success_message = 'Employee created successfully!'
                messages.success(request, success_message)
                return redirect('search/')
            except:
                pass
    else:
        form = EmployeeForm()
        # messages.success(request, success_message)
    # return render(request, 'create.html')
    return render(request, 'create.html', {'form':form})

# Search Blog
        
def retrieve_employee(request):
    employees = Employee.objects.all()
    return render(request,'search.html',{'employees':employees} )


# Update Employee Details
def update_employee(request,pk):
    employees = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employees)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employees)
        if form.is_valid():
            form.save()
            return redirect('/search')
        
    context = {
        'employees': employees,
        'form': form,
    }
    return render(request,'update.html',context)


#Delete Employee Details
def delete_employee(request,pk):
    employees = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employees.delete()
        return redirect('/search')
    context = {
        'employees': employees,
    }
    return render(request, 'delete.html', context)
