from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200, db_index=True)
    slug=models.SlugField(max_length=200, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    name=models.CharField(max_length=200, db_index=True)
    slug=models.SlugField(max_length=200, db_index=True)
    description=models.TextField(blank=True)
    sku = models.CharField(max_length=20, unique=True, null=True)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    brand = models.CharField(max_length=30, null=True)
    specification = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)   # media files

    class Meta:
        ordering = ('name',)
        unique_together = (("id", "slug"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_images',
                                on_delete=models.CASCADE,
                                null=True, blank=True)
    picture = models.ImageField(upload_to='product_images') # goes now to media/product_images instead to static

    def __str__(self):
        return self.picture.name  # was before .url
