from django.contrib import admin

from .models import Category, Service, BuyingHistory

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(BuyingHistory)
