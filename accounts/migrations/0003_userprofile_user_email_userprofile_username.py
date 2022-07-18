# Generated by Django 4.0.5 on 2022-07-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_userprofile_blood_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_email',
            field=models.EmailField(blank=True, max_length=70, unique=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=20, null=True, verbose_name='User Name'),
        ),
    ]