from django.shortcuts import render, redirect
from .models import Item


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
        name = request.POST.get('item_name')
        # Because boolean, checks if item has a 'done' property:
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
