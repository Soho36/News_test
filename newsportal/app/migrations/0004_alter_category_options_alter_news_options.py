# Generated by Django 4.2.13 on 2024-05-25 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_test'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
    ]