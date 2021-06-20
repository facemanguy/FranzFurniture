from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('types/', views.types, name='types'),
    path('furniturelist/', views.getFurniture, name='furniture'),
    path('furnituredetail/<int:id>', views.getFurnitureDetail, name='furnituredetail'),
    path('newfurniture/', views.newFurniture, name='newfurniture'),
]