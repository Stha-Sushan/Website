from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('listcategory/<int:pk>', views.listcategory, name='listcategory'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('cartitems/<int:pk>', views.cartitems, name='cartitems'),
    path('remove/<int:product>', views.remove, name='remove'),
    path('send_email', views.send_email, name='send_email'),
    path('email/', views.email, name='email'),

]