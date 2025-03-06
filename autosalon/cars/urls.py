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

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.LessonListView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', views.LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/create/', views.LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/update/', views.LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete/', views.LessonDeleteView.as_view(), name='lesson_delete'),
]

from django.urls import path
from .views import CarUpdateView

urlpatterns = [
    path('car/update/<int:pk>/', CarUpdateView.as_view(), name='car_update'),
]

from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]

from django.urls import path
from .views import CarSearchView, BrandSearchView

urlpatterns = [
    path('car/search/', CarSearchView.as_view(), name='car_search'),
    path('brand/search/', BrandSearchView.as_view(), name='brand_search'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Bosh sahifa view'ini sozlash
]
