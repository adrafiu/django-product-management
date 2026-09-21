from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    production_date = models.DateField()
    image = models.ImageField(upload_to='media/product_img', null=True)

    def __str__(self):
        return self.name