# Generated by Django 3.2.2 on 2021-05-13 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_articles_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='user',
            new_name='author',
        ),
    ]