from django.urls import path
from .views import RestaurantList, RestaurantDetail, MenuList, MenuDetail, ItemList, ItemDetail

urlpatterns = [
    path('restaurants/', RestaurantList.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),
    path('menus/', MenuList.as_view(), name='menu-list'),
    path('menus/<int:pk>/', MenuDetail.as_view(), name='menu-detail'),
    path('items/', ItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
]