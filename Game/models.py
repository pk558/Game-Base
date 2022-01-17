from django.db import models

class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Category";
        verbose_name_plural = "Categories"

class Platform(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Platform";
        verbose_name_plural = "Platforms"

class Games(models.Model):#stworzenie klasy Games
    def __str__(self):
        return f"{self.name}"
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    category = models.ManyToManyField(Category,default=None, blank=True)
    platform = models.ManyToManyField(Platform)
    image= models.ImageField(null=True,blank=True)


    class Meta:
        verbose_name = "Game";
        verbose_name_plural = "Games"


