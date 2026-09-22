from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('add_product/', views.add_product, name= 'add_product'),
    path('product_list/', views.product_list, name= 'product_list'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product')   

]    