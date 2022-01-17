from django.contrib import admin
from .models import Games,Category,Platform
# Register your models here.

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_filter=('category','platform')
    list_display=['id','name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display=['name']