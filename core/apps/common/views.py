from rest_framework import generics
from rest_framework.response import Response

from core.apps.common import models, serializers


class SiteConfigApiView(generics.GenericAPIView):
    queryset = models.SiteConfig.objects.all()
    serializer_class = serializers.SiteConfigSerializer
    
    def get(self, request):
        site_config = models.SiteConfig.objects.first()
        serializer = self.serializer_class(site_config)
        return Response(serializer.data, status=200)
    

class AboutUsApiView(generics.GenericAPIView):
    queryset = models.AboutUs.objects.all()
    serializer_class = serializers.AboutUsSerializer
    
    def get(self, request):
        about_us = models.AboutUs.objects.prefetch_related('images', 'features').first()
        serializer = self.serializer_class(about_us)
        return Response(serializer.data, status=200)
    

class BannerListApiView(generics.ListAPIView):
    serializer_class = serializers.BannerListSerializer
    queryset = models.Banner.objects.all()


class ServiceListApiView(generics.ListAPIView):
    serializer_class = serializers.ServiceListSerializer
    queryset = models.Service.objects.all()


class NewsListApiView(generics.ListAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = models.News.objects.all()


class ContactUsApiView(generics.CreateAPIView):
    serializer_class = serializers.ContactUsSerializer
    queryset = models.ContactUs.objects.all()
    