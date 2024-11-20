from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)
    def __str__(self):
        product_quantity = str(self.product_set.count())
        if product_quantity == '0':
            product_quantity = 'пусто'
        elif product_quantity == '1':
            product_quantity += ' продукт'
        else:
            product_quantity += ' продукта'
        return f"{self.category_name} - {product_quantity}"


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    have = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

