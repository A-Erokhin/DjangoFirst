from django.shortcuts import render, HttpResponse
from django.http import Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


# items = [
#     {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
#     {"id": 2, "name": "Куртка кожаная", "quantity": 2},
#     {"id": 5, "name": "Coca-cola Санкционая 1 литр", "quantity": 12},
#     {"id": 7, "name": "Картофель фри", "quantity": 0},
#     {"id": 8, "name": "Кепка", "quantity": 124},
# ]

# Create your views here.
def home(request):
    return render(request, 'index.html')

def page_item(request, id):
    try:
        item = Item.objects.get(id = id)
    except ObjectDoesNotExist:
        raise Http404(f"Товар с id={id} не найден")
    context = {
        "item": item
    }
    # if item.count == 0:
    #     item.count = "Нет на складе"
    return render(request, 'item_page.html', context)
    #

def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'items_list.html', context)
















