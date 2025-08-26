from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from core.apps.orders import models


@admin.register(models.Order)
class OrderAdmin(TranslationAdmin):
    list_display = ['name', 'user', 'total_price', 'status', 'is_paid']
    list_filter = ['is_paid', 'user', 'status']