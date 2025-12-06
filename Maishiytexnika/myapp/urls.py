from django.urls import include, path
from .views import texnika_detail, texnika_list, categories_page, create_texnika, update_texnika, delete_texnika
urlpatterns = [
    path('', categories_page, name='categories_page'),
    path('category/<int:pk>/', texnika_list, name='texnika_list'),
    path('products/<int:pk>/', texnika_detail, name='texnika_detail'),
    path('create-texnika/', create_texnika, name='create_texnika'),
    path('update-texnika/<int:pk>/', update_texnika, name='update_texnika' ),
    path('delete-texnika/<int:pk>/', delete_texnika, name='delete_texnika' ),

]