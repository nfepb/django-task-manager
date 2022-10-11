from django.shortcuts import render
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
