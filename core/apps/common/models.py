import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, db_index=True, default=uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Banner(BaseModel):
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)
    banner = models.ImageField(upload_to='banner/images/')

    def __str__(self):
        return self.banner.name
    
    def delete(self, *args, **kwargs):
        if self.banner:
            self.banner.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'bannerlar'


class AboutUs(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'biz haqimizda'
        verbose_name_plural = 'biz haqimizda'


class AboutUsImage(BaseModel):
    image = models.ImageField(upload_to='about_us/images/')
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.about_us} image {self.image.name}'
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        return super().delete(*args, **kwargs)
    

class AboutUsFeature(BaseModel):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='features')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Service(BaseModel):
    title = models.CharField(max_length=200)
    text = models.TextField()
    icon = models.ImageField(upload_to='service/icons/')
    image = models.ImageField(upload_to='service/images/')

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.icon:
            self.icon.delete(save=False)
        if self.image:
            self.image.delete(save=False)
        return super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Xizmatlar'
        verbose_name_plural = 'Xizmatlarimiz'


class ContactUs(BaseModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='contract_us')
    message = models.TextField()
    is_contacted = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'ariza'
        verbose_name_plural = 'arizalar'


class News(BaseModel):
    image = models.ImageField(unique='news/images/')
    title = models.CharField(max_length=300)
    text = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'yangilik'
        verbose_name_plural = 'yangiliklar'


class SiteConfig(BaseModel):
    telegram = models.URLField()
    facebook = models.URLField()
    youtube = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return 'site config'
    
    class Meta:
        verbose_name = 'sayt sozlamalari'
        verbose_name_plural = 'sayt sozlamalari'


class Country(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Davlat'
        verbose_name_plural = 'Davlatlar'

    
class Requisite(BaseModel):
    company_name = models.CharField(max_length=200)
    legal_address = models.CharField(max_length=200)
    tin = models.CharField(max_length=15)
    okpo = models.CharField(max_length=10)
    oked = models.CharField(max_length=10)
    bank_name = models.CharField(max_length=200)
    bank_code = models.CharField(max_length=15)
    uzs = models.PositiveBigIntegerField()
    usd = models.PositiveBigIntegerField()

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'korxona rekvizit'
        verbose_name_plural = 'korxona rekvizitlar'
    

class PrivacyPolicy(BaseModel):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Maxfiylik siyosati'
        verbose_name_plural = 'Maxfiylik siyosati'
