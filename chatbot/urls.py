from django.urls import path
from .views import get_recipe, index , login , signup , add_user , login_view , add_favorite , view_favorites

urlpatterns = [
    path('', index, name='index'),
    # path('index/' , index , name='index'),
    path('get-recipe/', get_recipe, name='get_recipe'),
    path('login/', login_view, name='login'),
    path('signup/', signup ),
    path('add-user/', add_user, name='add_user'),
    # path('success/', success, name='success'),  
    path('add-favorite/', add_favorite, name='add_favorite'),
    path('favorites/', view_favorites, name='view_favorites'),
]
