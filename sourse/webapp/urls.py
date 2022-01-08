
from django.urls import path

from webapp.views import main_page, create

urlpatterns = [
    path('', main_page, name="main"),
    path('book/create/', create, name="create")

]