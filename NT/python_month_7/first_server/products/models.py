from django.db import models



class Service(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=60)

class Categories(models.Model):
    name = models.CharField(max_length=20)

class Countries(models.Model):
    name = models.CharField(max_length=30)


class DiscountProducts(models.Model):
    class DiscountTypes(models.TextChoices):
        s = 'USD', '$'
        f = 'FOIZ', '%'
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='products/discount')
    quantity = models.IntegerField()
    discount_type = models.CharField(max_length=20, choices=DiscountTypes.choices, default=DiscountTypes.f)

class Products(models.Model):

    class PryceType(models.TextChoices):
        usd = 'USD', '$'
        sum = 'UZS', 'so`m'

    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    price_type = models.CharField(max_length=20, choices=PryceType.choices, default=PryceType.usd)
    image = models.ImageField(upload_to='products/product')
    benefits = models.TextField()
    countries = models.ManyToManyField(Countries)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    min_weight = models.FloatField()
    taken_time = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

