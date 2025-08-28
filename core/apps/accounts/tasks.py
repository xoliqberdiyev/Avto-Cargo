from celery import shared_task

from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_confirmation_email(user_email, code):
    from django.core.mail import EmailMultiAlternatives

    subject = "Код подтверждения для WISDOM Cargo"
    from_email = settings.EMAIL_HOST_USER
    to = [user_email]

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <style>
        body {{
          font-family: Arial, sans-serif;
          background-color: #f4f6f8;
          margin: 0;
          padding: 0;
        }}
        .container {{
          max-width: 600px;
          background: #ffffff;
          margin: 30px auto;
          padding: 30px;
          border-radius: 12px;
          box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        h2 {{
          color: #333333;
        }}
        .code-box {{
          margin: 20px 0;
          padding: 15px;
          background: #f0f9ff;
          border: 1px dashed #007bff;
          text-align: center;
          font-size: 24px;
          font-weight: bold;
          letter-spacing: 3px;
          color: #007bff;
          border-radius: 8px;
        }}
        p {{
          color: #555555;
          font-size: 15px;
          line-height: 1.6;
        }}
        .footer {{
          margin-top: 30px;
          font-size: 13px;
          color: #999999;
          text-align: center;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <h2>Код подтверждения для WISDOM Cargo</h2>
        <p>Уважаемый <strong>{user_email}</strong>,</p>
        <p>Для завершения процесса регистрации на платформе <b>Avto Cargo</b>, пожалуйста, используйте следующий код подтверждения:</p>
        <div class="code-box">{code}</div>
        <p>Пожалуйста, используйте этот код в течение <b>5 минут</b> для завершения регистрации.</p>
        <p>Если код не работает или вам нужна дополнительная помощь, свяжитесь с нами по адресу 
        <a href="mailto:wisdomcargo1@gmail.com">wisdomcargo1@gmail.com</a>.</p>
        <div class="footer">
          С уважением,<br>
          Команда Wisdom Cargo
        </div>
      </div>
    </body>
    </html>
    """

    msg = EmailMultiAlternatives(subject, "", from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()