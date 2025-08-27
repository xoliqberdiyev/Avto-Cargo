from modeltranslation import translator

from core.apps.orders.models import Order


@translator.register(Order)
class OrderTranslation(translator.TranslationOptions):
    fields = [
        'name', 'location'
    ]