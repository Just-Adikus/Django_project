from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html', {'title': 'Главная страница'})

def about(request):
    return render(request, 'about.html', {'title': 'О нас'})

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return render(request, 'result.html', {'name': name})
    return render(request, 'form.html', {'title': 'Форма ввода данных'})

def page_not_found(request, exception):
    return render(request, '404.html', {'title': 'Страница не найдена'}, status=404)

