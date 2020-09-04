from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(User.username, max_length=20)
    apellidos = models.CharField(User.last_name, max_length=20)
    email = models.CharField(User.email, max_length=100)


class Category(models.Model):
    title = models.CharField(max_length=225, default='')
    def __str__(self):
        return self.title


class Producto(models.Model):
    title = models.CharField(max_length=30, default='')
    descripcion = models.TextField(default='')
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    image = models.ImageField(default='', blank=True, upload_to='image')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(300,200)], format="JPEG", options={'quality': 60})
    precio = models.FloatField(max_length=5, default='')

    def __str__(self):
        return self.title


