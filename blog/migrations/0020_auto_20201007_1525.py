# Generated by Django 2.2.5 on 2020-10-07 14:25

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20201007_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='body', unique_with=('created__month',)),
        ),
    ]
