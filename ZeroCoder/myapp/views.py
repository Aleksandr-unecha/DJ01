from django.http import HttpResponse

def data_view(request):
    return HttpResponse("<h1>Это страница data</h1>")

def test_view(request):
    return HttpResponse("<h1>Это страница test</h1>")

def home_view(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")