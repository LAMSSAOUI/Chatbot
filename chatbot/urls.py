from django.urls import path
from .views import get_recipe, index , login

urlpatterns = [
    path('', index, name='index'),
    path('get-recipe/', get_recipe, name='get_recipe'),
    path('login/', login, name='get_recipe'),
]
