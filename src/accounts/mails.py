from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import OTP, User


def send_reset_mail(user_id):
    user: User = User.objects.get(id=user_id)
    code: OTP = OTP.objects.get(user__id=user_id).code
    subject = "Reset Password"
    from_mail = f"<{settings.DEFAULT_FROM_EMAIL}>"
    to_mail = user.email

    text_content = render_to_string(
        "accounts/emails/password_reset.txt",
        context={"code": code},
    )

    # html_content = render_to_string(
    #     "accounts/emails/password_reset.html",
    #     context={"code": code},
    # )

    msg = EmailMultiAlternatives(
        subject,
        text_content,
        from_mail,
        [to_mail],
    )

    # msg.attach_alternative(html_content, "text/html")
    return msg.send(fail_silently=False)
