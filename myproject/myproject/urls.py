from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_laptops, name='list_laptops'),
    path('add/', views.add_laptop, name='add_laptop'),
    path('update/<int:pk>/', views.update_laptop, name='update_laptop'),
    path('delete/<int:pk>/', views.delete_laptop, name='delete_laptop'),
]
