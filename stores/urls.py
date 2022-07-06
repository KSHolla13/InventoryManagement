from django.urls import path
from . import views

urlpatterns = [
    path('', views.Reader, name = 'Reader'),
    path('home', views.home, name = 'home'),
    path('home/delete/<int:id>', views.delete_book, name = 'delete_book'),
    path('home/edit/<int:id>', views.edit_book, name = 'edit_book'),
    path('storelist', views.storelist, name = 'storelist'),
    path('storelist/collection', views.collection, name = 'collection'),
    path('contact', views.contact, name = 'contact'),
    path('home/Addbook', views.Addbook, name = 'Addbook')

]