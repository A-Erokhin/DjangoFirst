from django.shortcuts import render, HttpResponse

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

def item(reqest, id):
    pos = id - 1
    if pos < 5:
        text = f"""
            Артикул: <b>{items[pos]['id']}</b><br>
            Название: <b>{items[pos]['name']}</b><br>
            Количество: <b>{items[pos]['quantity']}</b><br/> 
            """
    else:
        text = f"Товар с id={id} не найден"
    return HttpResponse(text)