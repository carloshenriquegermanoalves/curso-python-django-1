from django.urls import path

from books.views import my_view, home, contato

urlpatterns = [
    path('', my_view),
    path('sobre/', home),
    path('contato/', contato)
]
