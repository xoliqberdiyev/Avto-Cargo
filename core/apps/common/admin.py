from django.contrib import admin 

from django.http import HttpResponseRedirect
from django.urls import reverse
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from core.apps.common import models


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['banner']


@admin.register(models.SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=...):
        return False
    
    def changelist_view(self, request, extra_context=None):
        config, create = models.SiteConfig.objects.get_or_create(
            defaults=dict(
                telegram='https://t.me/telegram',
                facebook='https://facebook.com',
                instagram='https://instagram.com',
                youtube='https://youtube.com',
            )
        )
        url = reverse('admin:common_siteconfig_change', args=[config.id])
        return HttpResponseRedirect(url)
    

class AboutUsImageInline(admin.TabularInline):
    model = models.AboutUsImage
    extra = 0
    verbose_name = 'rasm'
    verbose_name_plural = 'rasmlar'


class AboutUsFeatureInline(TranslationTabularInline):
    model = models.AboutUsFeature
    extra = 0
    verbose_name = 'xususiyat'
    verbose_name_plural = 'xususiyatlar'


@admin.register(models.AboutUs)
class AboutUsAdmin(TranslationAdmin):
    list_display = ['title', 'description']
    inlines = [AboutUsImageInline, AboutUsFeatureInline]
    
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True


@admin.register(models.Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ['title', 'text', 'icon', 'image']
    

@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        'email', 'phone', 'is_contacted'
    ]

    def has_add_permission(self, request):
        return False


@admin.register(models.News)
class NewsAdmin(TranslationAdmin):
    list_display = ['title', 'text', 'image']


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']