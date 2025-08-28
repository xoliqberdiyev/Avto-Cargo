from modeltranslation import translator

from core.apps.common import models


@translator.register(models.Banner)
class BannerTranslation(translator.TranslationOptions):
    fields = [
        'title', 'text' 
    ]
    

@translator.register(models.AboutUs)
class AboutUsTranslation(translator.TranslationOptions):
    fields = [
        'title', 'description',
    ]


@translator.register(models.AboutUsFeature)
class AboutUsFeatureTranslation(translator.TranslationOptions):
    fields = [
        'text'
    ]


@translator.register(models.Service)
class ServiceTranslation(translator.TranslationOptions):
    fields = [
        'title', 'text',
    ]


@translator.register(models.News)
class NewsTranslation(translator.TranslationOptions):
    fields = [
        'title', 'text'
    ]
