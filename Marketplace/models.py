from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name', ]

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000000)
    image = models.ImageField(upload_to='Market_place/item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
