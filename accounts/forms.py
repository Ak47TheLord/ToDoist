from django import forms
from accounts.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # exclude = ["user", "image", "role"]
        fields = ["username", "user_email", "cnic", "primary_phone", "secondary_phone", "address"]
        widgets = {
            "address": forms.Textarea(attrs={"col_cls": "col-md-11"}),
            "cnic": forms.TextInput(attrs={"col_cls": "col-md-4"}),
        }


class UserProfileImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["image"]
