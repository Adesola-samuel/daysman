# Generated by Django 2.2.5 on 2020-11-03 05:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20201007_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
