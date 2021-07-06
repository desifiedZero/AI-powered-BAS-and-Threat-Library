# Generated by Django 3.2.1 on 2021-07-05 20:56

from django.conf import settings
from django.contrib.auth.models import User
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_user', '0004_appuser_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user'),
            preserve_default=False,
        ),
    ]
