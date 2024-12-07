from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop
from .forms import LaptopForm

# Create Laptop
def add_laptop(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_laptops')
    else:
        form = LaptopForm()
    return render(request, 'laptop/add_laptop.html', {'form': form})

def list_laptops(request):
    laptops = Laptop.objects.all()
    return render(request, 'laptop/list_laptops.html', {'laptops': laptops})


# Update Laptop
def update_laptop(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    if request.method == "POST":
        form = LaptopForm(request.POST, instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('list_laptops')
    else:
        form = LaptopForm(instance=laptop)
    return render(request, 'laptop/update_laptop.html', {'form': form})

# Delete Laptop
def delete_laptop(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    if request.method == "POST":
        laptop.delete()
        return redirect('list_laptops')
    return render(request, 'laptop/delete_laptop.html', {'laptop': laptop})
