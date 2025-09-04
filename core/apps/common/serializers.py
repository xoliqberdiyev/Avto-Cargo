from rest_framework import serializers

from core.apps.common import models


class SiteConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiteConfig
        fields = [
            'telegram', 'instagram', 'youtube', 'facebook'
        ]
    

class AboutUsFeatureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutUsFeature
        fields = [
            'id', 'text'
        ]


class AboutUsImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutUsImage
        fields = [
            'id', 'image'
        ]


class AboutUsSerializer(serializers.ModelSerializer):
    images = AboutUsImageListSerializer(many=True)
    features = AboutUsFeatureListSerializer(many=True)

    class Meta:
        model = models.AboutUs
        fields = [
            'id', 'title', 'description', 'images', 'features' 
        ]


class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = [
            'id', 'banner', 'title', 'text'
        ]


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = [
            'id', 'title', 'text', 'icon', 'image',
        ]


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ['id', 'image', 'title', 'text']
    

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = [
            'first_name', 'last_name', 'phone', 'email', 'service', 'message',
        ]
    

class RequisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Requisite
        fields = [
            'id', 'company_name', 'legal_address', 'tin', 'okpo', 'oked', 'bank_name', 'bank_code',
            'uzs', 'usd',
        ]


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrivacyPolicy
        fields = [
            'id', 'title', 'text'
        ]


class UserTermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserTerms
        fields = [
            'id', 'text'
        ]