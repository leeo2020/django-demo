# Generated by Django 3.2.2 on 2021-05-13 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_articles_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='user',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author', verbose_name='author'),
        ),
    ]