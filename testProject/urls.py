
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def index(request):
    return HttpResponse('<h1>Hello this is a test project for heroku</h1>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]
