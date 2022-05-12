from django.urls import path
from . import views
urlpatterns = [
    path("",views.home, name="home"),
    # path("",views.users, name="users"),
    # path("",views.shop, name="shop")
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),
    path('products/cart/',views.cart,name='cart',),
     
]


'''
path('home/',TemplateView.as_view(template_name='dashboard/home.html'),name='home'),
    path('users/',TemplateView.as_view(template_name='dashboard/users.html'),name='users'),
    path('products/',TemplateView.as_view(template_name='dashboard/products.html'),name='products'),
    path('customer/',TemplateView.as_view(template_name='dashboard/customer.html'),name='customer'),
    path('cart/',TemplateView.as_view(template_name='dashboard/cart.html'),name='cart'),
   
'''