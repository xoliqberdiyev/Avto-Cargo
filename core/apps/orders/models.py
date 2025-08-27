from django.db import models

from core.apps.common.models import BaseModel
from core.apps.accounts.models import User
from core.apps.common.models import Country


class Order(BaseModel):
    STATUS = (
        ('Yetkazilmoqda', 'Yetkazilmoqda'),
        ('Olingan', 'Olingan'),
        ('Kutilmoqda', 'Kutilmoqda'),
        ('Yetkazib berilgan', 'Yetkazib berilgan')
    )

    order_number = models.PositiveBigIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    name = models.CharField(max_length=200)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS)
    size = models.CharField(max_length=20)
    total_price = models.PositiveBigIntegerField()
    is_paid = models.BooleanField(default=False)
    location = models.CharField(max_length=200)
    location_to = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='location_to')
    location_from = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='location_from')

    def __str__(self):
        return f'{self.user} user order {self.name}'
    
    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'buyurtmalar'
    