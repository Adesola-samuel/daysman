# Generated by Django 3.2.5 on 2022-01-26 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0007_auto_20220126_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='profile',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]