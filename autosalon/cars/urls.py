from django.urls import path
from .views import home, cars_by_color, cars_by_brand, car_detail, add_comment, register
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]



urlpatterns = [

    path('', home, name='home'),
    path('color/<int:color_id>/', cars_by_color, name='cars_by_color'),
    path('brand/<int:brand_id>/', cars_by_brand, name='cars_by_brand'),
    path('car/<int:car_id>/', car_detail, name='car_detail'),
    path('car/<int:car_id>/comment/', add_comment, name='add_comment'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]