from django.shortcuts import render, redirect
from .forms import EmployeeForm
# import sys

def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('search/')
            except:
                pass
    else:
        form = EmployeeForm()
        # var_name = {'name': 'muthu'}
        # print(var_name)
        # sys.exit()

    return render(request, 'create.html', {'form':form})

# Search Blog
        
def retrieve_employee(request):
    employee = employee.objects.all()
    return render(request,'search.html',{'employee':employee} )