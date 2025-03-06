from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from pyexpat.errors import messages
from django.views import View



from .models import Car, Color, Brand, Comment
from django.contrib.auth.decorators import login_required

def home(request):
    cars = Car.objects.all()
    return render(request, 'cars/home.html', {'cars': cars})

def cars_by_color(request, color_id):
    color = get_object_or_404(Color, id=color_id)
    cars = Car.objects.filter(color=color)
    return render(request, 'cars/car_list.html', {'cars': cars, 'filter_type': f"Rang: {color.name}"})

def cars_by_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    cars = Car.objects.filter(brand=brand)
    return render(request, 'cars/car_list.html', {'cars': cars, 'filter_type': f"Brend: {brand.name}"})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    comments = car.comments.all()
    return render(request, 'cars/car_detail.html', {'car': car, 'comments': comments})

@login_required
def add_comment(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        text = request.POST.get('text')
        if text:
            Comment.objects.create(car=car, user=request.user, text=text)
        return redirect('car_detail', car_id=car.id)
    return render(request, 'cars/add_comment.html', {'car': car})

from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})







from django.core.mail import send_mail
from django.contrib.auth.models import User


def add_car(request):
    if request.method == "POST":
        name = request.POST['name']
        brand_id = request.POST['brand']
        color_id = request.POST['color']
        price = request.POST['price']

        brand = Brand.objects.get(id=brand_id)
        color = Color.objects.get(id=color_id)

        car = Car.objects.create(name=name, brand=brand, color=color, price=price)

        # Email yuborish
        users = User.objects.all()
        recipient_list = [user.email for user in users if user.email]
        if recipient_list:
            send_mail(
                'New Car Added',
                f'A new car "{car.name}" has been added!',
                'admin@myproject.com',  # Sender email
                recipient_list,
                fail_silently=False,
            )

        return redirect('home')

    brands = Brand.objects.all()
    colors = Color.objects.all()
    return render(request, 'cars/add_car.html', {'brands': brands, 'colors': colors})

def home(request):
    return render(request, 'cars/home.html')


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Lesson
from django.urls import reverse_lazy


class LessonListView(ListView):
    model = Lesson
    template_name = 'lessons/lesson_list.html'
    context_object_name = 'lessons'


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lessons/lesson_detail.html'
    context_object_name = 'lesson'


class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'lessons/lesson_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('lesson_list')


class LessonUpdateView(UpdateView):
    model = Lesson
    template_name = 'lessons/lesson_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('lesson_list')


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'lessons/lesson_confirm_delete.html'
    context_object_name = 'lesson'
    success_url = reverse_lazy('lesson_list')


from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import LessonForm

class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'cars/lesson_form.html'
    success_url = '/lesson/create/'

from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import Car

class CarUpdateView(UpdateView):
    model = Car
    fields = ['name', 'brand', 'category', 'price']  # kerakli maydonlarni qo'shing
    template_name = 'cars/car_form.html'  # form uchun shablon
    success_url = '/cars/'  # muvaffaqiyatli yangilashdan keyin qayerga yo'naltirish


from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Category
from django.urls import reverse_lazy

# Category List
class CategoryListView(ListView):
    model = Category
    template_name = 'cars/category_list.html'
    context_object_name = 'categories'

# Category Create
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'cars/category_form.html'
    success_url = reverse_lazy('category_list')

# Category Update
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'cars/category_form.html'
    success_url = reverse_lazy('category_list')

# Category Delete
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'cars/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

from django.db.models import Q
from django.views.generic import ListView
from .models import Car, Brand

# Car search
class CarSearchView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Car.objects.filter(Q(name__icontains=query) | Q(brand__name__icontains=query))
        return Car.objects.all()

# Brand search
class BrandSearchView(ListView):
    model = Brand
    template_name = 'cars/brand_list.html'
    context_object_name = 'brands'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Brand.objects.filter(name__icontains=query)
        return Brand.objects.all()

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'
    paginate_by = 10  # 10 ta mashina bir sahifada

class CategoryListView(ListView):
    model = Category
    template_name = 'cars/category_list.html'
    context_object_name = 'categories'
    paginate_by = 5  # 5 ta kategoriya bir sahifada


from django.http import HttpResponse
#
# def home(request):
#     return HttpResponse("Welcome to the home page!")

