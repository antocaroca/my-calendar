from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """
    last_name = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=12)
    city = forms.CharField(max_length=255)
    region = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)

    def signup(self, request, user):
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']
        user.city = self.cleaned_data['city']
        user.region = self.cleaned_data['region']
        user.country = self.cleaned_data['country']
        user.save()
        return user
    


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
