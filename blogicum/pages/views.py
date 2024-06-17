from django.shortcuts import render


def about(request):
    """Отображение страницы с описанием сайта."""
    return render(request, 'pages/about.html')


def rules(request):
    """Отображение страницы с правилами сайта."""
    return render(request, 'pages/rules.html')
