from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, null=True, blank=False, verbose_name="User Name")
    user_email = models.EmailField(max_length=70, blank=True, unique=True)
    cnic = models.CharField(max_length=20, null=True, blank=False, verbose_name="CNIC")
    primary_phone = models.CharField(max_length=20, null=True, blank=False)
    secondary_phone = models.CharField(max_length=20, null=True, blank=True, help_text="Optional")
    image = models.ImageField(upload_to="users/", null=True, blank=True, default="users/dummy.jpg")
    address = models.TextField(max_length=200, null=True, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
