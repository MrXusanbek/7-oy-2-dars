from django.contrib import admin
from .models import Color, Brand, Car, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'color', 'price')
    inlines = [CommentInline]

admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Car, CarAdmin)
admin.site.register(Comment)
