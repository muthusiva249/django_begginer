from django.urls import path
from . import views

urlpatterns = [
    path('door_details', views.create_door, name='create-door'),
    path('shop_door', views.shop_door, name='shop-door'),
    # path('update/<int:pk>', views.update_employee, name='update-employee'),
    # path('delete/<int:pk>', views.delete_employee, name='delete-employee'),
]