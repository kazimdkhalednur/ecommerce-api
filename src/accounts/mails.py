from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import OTP, User


def send_verification_mail(uidb64, user_mail, token, use_https, site_name, domain):
    subject = "Verify Your Email Address"
    from_mail = f"<{settings.DEFAULT_FROM_EMAIL}>"
    to_mail = user_mail

    text_content = render_to_string(
        "accounts/emails/verification_email.txt",
        context={
            "uidb64": uidb64,
            "token": token,
            "site_name": site_name,
            "domain": domain,
            "protocol": "https" if use_https else "http",
        },
    )

    # html_content = render_to_string(
    #     "accounts/emails/verification_email.html",
    #     context={
    #         "site_name": site_name,
    #         "domain": domain,
    #         "token": token_generator.make_token(user),
    #         "uid": user.id,
    #         "protocol": "https" if use_https else "http",
    #     },
    # )

    msg = EmailMultiAlternatives(
        subject,
        text_content,
        from_mail,
        [to_mail],
    )

    # msg.attach_alternative(html_content, "text/html")
    return msg.send(fail_silently=False)


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
