from django.shortcuts import render, HttpResponse
from django.http import Http404
from MainApp.models import Item


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
    item = Item.objects.get(id = id)
    # for item in items:
    #     if item['id'] == id:
    context = {
                "item": item
            }
    return render(request, 'item_page.html', context)
    # raise Http404(f"Товар с id={id} не найден")

def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'items_list.html', context)
















