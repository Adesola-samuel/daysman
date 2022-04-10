# Generated by Django 2.2.5 on 2020-09-29 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postdislike',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='postdislike',
            name='users',
        ),
        migrations.RenameField(
            model_name='commentlike',
            old_name='users',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='postlike',
            old_name='users',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published',
        ),
        migrations.DeleteModel(
            name='CommentDisLike',
        ),
        migrations.DeleteModel(
            name='PostDisLike',
        ),
    ]
