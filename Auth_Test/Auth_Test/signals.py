import email
from allauth.socialaccount.signals import pre_social_login
from django.dispatch import receiver


@receiver(pre_social_login)
def save_email_address(request, user, **kwargs):
    email = request.data.email
    email.save()