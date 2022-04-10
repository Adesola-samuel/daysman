# Generated by Django 3.2.5 on 2022-02-11 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academy', '0012_level_class_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='class_teacher',
        ),
        migrations.CreateModel(
            name='Clas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clas', models.CharField(choices=[('Choose', ''), ('Jss1', 'Jss1'), ('Jss2', 'Jss2'), ('Jss3', 'Jss3'), ('Sss1', 'Sss1'), ('Sss3', 'Sss2'), ('Sss3', 'Sss3')], max_length=10)),
                ('class_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='level',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.clas'),
        ),
    ]
