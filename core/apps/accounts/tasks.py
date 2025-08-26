from celery import shared_task

from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_confirmation_code_to_email(email, code):
    send_mail(
        "Avto Cargo uchun tasdiqlash kod.",
        f"Bu sizning tasdiqlash kodingiz: {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
