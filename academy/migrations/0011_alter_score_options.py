# Generated by Django 3.2.5 on 2022-01-30 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0010_score_student'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['level', 'subject']},
        ),
    ]
