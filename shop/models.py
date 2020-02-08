from django.db import models
from django.urls import reverse
from django.utils import timezone
from mysite import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='awaiting')

class Product(models.Model):
    STATUS_CHOISES = (
        ("awaiting", 'Ожидает действий'),
        ('confirmed', 'Подтвержден'),
        ('done', 'Выполнен'),
    )
    TYPE_CHOISES = (
        ('figure', "Фигурка"),
        ('earring', "Серьги"),
        ('necklace', "Кулон"),
    )
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=10, choices=TYPE_CHOISES)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images', blank=True)
    # status = models.CharField(max_length=10, choices=STATUS_CHOISES, null=True, blank=True)
    # clients = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True)
    rate = models.PositiveIntegerField(null=True, blank=True)
    # cart = PublishedManager()
    objects = models.Manager()

    class Meta:
        ordering = ('-price',)

    def __str__(self):
        return self.name



class Purchase(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='basket', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField()

    @property
    def cost(self):
        return self.product.price * self.count

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'comment by {} on {}'.format(self.name, self.product)
