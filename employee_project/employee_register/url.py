from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_employee, name='create-employee'),
    path('search/', views.retrieve_employee, name='retrieve-employee'),
    path('update/<int:pk>', views.update_employee, name='update-employee')
    # path('delete/<int:pk>', views.delete_employee, name='delete-employee'),
]