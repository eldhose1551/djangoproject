from django.urls import path, include
from . import views

# app_name = 'textileapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.oneitem),

    path('<int:id>/delete/', views.delete),
    path('add/', views.add, name='add'),

    path('login/', views.log, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('register/', views.reg, name='register'),
    path('search/', views.search, name='search'),
    path('search/<int:id>/', views.searchitem, name='searchitem'),

    path('blog/', views.blog, name='blog'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart1, name='cart'),
    path('buynow/<int:id>/', views.buynow, name='buynow'),
    path('removecart/<int:id>/', views.removecart, name='removecart'),



]
