from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    """
    Default custom user model for Mi Calendario Auditivo.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    last_name = models.CharField(_("Lastname"), blank=True, max_length=255)
    phone = models.CharField(_("Phone"), blank=True, max_length=255)
    city = models.CharField(_("City"), blank=True, max_length=255)
    region = models.CharField(_("Region"), blank=True, max_length=255)
    country = models.CharField(_("Country"), blank=True, max_length=255, default='Chile')


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
