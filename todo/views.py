from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


# Create your views here.
def get_todo_list(request):
    # Query to get all items in db:
    items = Item.objects.all()
    # Dictionnary with all our items:
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # Creates a form instance in view to have db ruling over fields
    form = ItemForm()
    # Creates a context with an empty form and adds to template
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)
