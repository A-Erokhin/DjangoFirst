from django.shortcuts import render, HttpResponse
from django.http import Http404

author = {
    "name": "Александр",
    "surname": "Ерохин",
    "email": "a-erokhin@yandex.ru",
    "phone": "+7-999-999-99-99"
}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola Санкционая 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]

# Create your views here.
def home(request):
    text = f"""
    <h1>"Изучаем django"</h1>
    <b>Автор</b>: <i>Ерохин А.П.</i>
    """
    return HttpResponse(text)

def about(request):
    text = f"""
    Имя: <b>{author['name']}</b><br>
    Фамилия: <b>{author['surname']}</b><br>
    телефон: <b>{author['phone']}</b><br/> 
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse(text)

def page_item(reqest, id):
    for item in items:
        if item['id'] == id:
            text = f"""
                Название: <b>{item['name']}</b><br>
                Количество: <b>{item['quantity']}</b><br/> 
                """
            return HttpResponse(text)
    raise Http404(f"Товар с id={id} не найден")

def items_list(reqest):
    text = """
    <ol>
    """
    for item in items:
        text += f"<a href='/item/{item['id']}'><li>{item['name']}</li></a>"
    text += "</ol>"
    return HttpResponse(text)