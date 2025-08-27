from django.db import models

from core.apps.common.models import BaseModel
from core.apps.accounts.models import User


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
    location_to = models.CharField(max_length=200, null=True)
    location_from = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.user} user order {self.name}'
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            last_order = Order.objects.all().order_by('-order_number').first()
            if last_order:
                self.order_number = last_order.order_number + 1
            else:
                self.order_number = 1
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'buyurtmalar'
    