from django.contrib import admin
from django.utils.datetime_safe import datetime
from .models import Product, Purchase, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

admin.site.register(Product)
admin.site.register(Purchase)


