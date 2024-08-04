from django.db import models

# Create your models here.
class Product(models.Model):

    image = models.ImageField('Product image', upload_to = 'main_images')
    name = models.CharField('Product name', max_length = 60)
    price = models.PositiveIntegerField('Product price')

    def __str__(self):

        return self.name