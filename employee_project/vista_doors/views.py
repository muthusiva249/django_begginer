from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import DoorForm
from .models import Door
from django.urls import reverse

# from .models import Door  # Import your Door model

def create_door(request):
    if request.method == 'POST':
        form = DoorForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print("Form is valid")  # Add a print statement to check validity
            form.save()
            return redirect('/vista_doors/door_details')
        else:
            print("Form is not valid:", form.errors)  # Print form errors for debugging
    else:
        form = DoorForm()
    return render(request, 'create_door.html', {'form': form})


def shop_door(request):
    doors = Door.objects.exclude(door_image='')
    # doors = Door.objects.all()
    return render(request, 'shop_door.html', {'doors': doors})
