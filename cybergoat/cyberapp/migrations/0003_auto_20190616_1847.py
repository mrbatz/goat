# Generated by Django 2.2.2 on 2019-06-16 18:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cyberapp', '0002_auto_20190616_1846'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserForm',
            new_name='UserProfileInfoForm',
        ),
    ]
