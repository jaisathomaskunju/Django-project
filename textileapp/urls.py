from django.urls import path, include
from . import views

app_name = 'textileapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.oneitem, name='oneitem'),

    path('<int:id>/delete/', views.delete),
    path('add/', views.add, name='add'),

    path('login/', views.log, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('register/', views.reg, name='register'),
    path('search/', views.search, name='search'),
    path('search/<int:id>/', views.searchitem, name='searchitem'),

    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('checkout/<int:id>/', views.checkout, name='checkout'),
    path('delete_cart/<int:id>/', views.delete_cart, name='delete_cart'),
    # path('addtocart/<int:id>/', views.add_to_cart, name='addtocart'),
    # path('coupon/', views.coupon, name='coupon')
]
