from django.urls import path
from .views import home, flower_by_type, about_flowers, add_flower, add_type, update_flower, delete_flower

urlpatterns = [
    path('', home, name="home"),
    path('types/<int:type_id>/', flower_by_type, name='flower_by_type'),
    path('flowers/<int:flower_id>', about_flowers, name='about_flowers'),
    path('flowers/<int:flower_id>/update', update_flower, name='update_flower'),
    path('flowers/<int:flower_id>/delete', delete_flower, name='delete_flower'),
    path('add/flowers/', add_flower, name='add_flower'),
    path('add/type/', add_type, name='add_type'),
]