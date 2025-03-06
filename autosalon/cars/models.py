from django.db import models
from django.contrib.auth.models import User
# from .models import Category


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return f"{self.brand.name} {self.name}"

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.car.name}"




from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


from django.db import models



# models.py
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField(null=True)

    def __str__(self):
        return self.title




class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name







