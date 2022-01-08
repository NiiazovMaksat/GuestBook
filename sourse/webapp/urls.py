
from django.urls import path

from webapp.views import main_page, create, delete, edit

urlpatterns = [
    path('', main_page, name="main"),
    path('book/create/', create, name="create"),
    path('book/<int:pk>/edit/', edit, name="edit"),
    path('book/<int:pk>/delete/', delete, name="delete")
]