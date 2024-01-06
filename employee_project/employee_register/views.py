from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EmployeeForm
from .models import Employee
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pprint import pprint
from django.http import HttpResponse

## create employee
def create_employee(request):
    success_message = None
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                success_message = 'Employee created successfully!'
                messages.success(request, success_message)
                # return redirect(reverse('create-employee'))
                return redirect('retrieve-employee')
            except:
                pass
    else:
        form = EmployeeForm()
    # return render(request, 'create.html')
    return render(request, 'create.html', {'form':form})

## Employee list
def retrieve_employee(request):
    contact_filter = request.GET.get('contact', '')
    email_filter   = request.GET.get('email', '')
    employee = Employee.objects.all()
    if contact_filter:
        employee = employee.filter(contact=contact_filter)
    if email_filter:
        employee = employee.filter(email=email_filter)    
    employee = employee.order_by('-id')

    # Pagination logic
    items_per_page = 20
    paginator = Paginator(employee, items_per_page)
    page = request.GET.get('page', 1)
    try:
        employees_page = paginator.page(page)
    except PageNotAnInteger:
        employees_page = paginator.page(1)
    except EmptyPage:
        employees_page = paginator.page(paginator.num_pages)

    return render(request, 'search.html', {'employee': employees_page, 'contact_filter': contact_filter,'email_filter': email_filter})