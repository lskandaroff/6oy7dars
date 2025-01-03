from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('types/<int:type_id>/', flower_by_type, name='flower_by_type'),
    path('flowers/<int:flower_id>', about_flowers, name='about_flowers'),
    path('flowers/<int:flower_id>/update', update_flower, name='update_flower'),
    path('flowers/<int:flower_id>/delete', delete_flower, name='delete_flower'),
    path('add/flowers/', add_flower, name='add_flower'),
    path('add/type/', add_type, name='add_type'),
    path('auth/register/', register, name='register'),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),
    path('flowers/<int:flower_id>/comment/save/', comment_save, name="comment_save"),
    path('flowers/comment/<int:flower_id>/delete', comment_delete, name='comment_delete')
]