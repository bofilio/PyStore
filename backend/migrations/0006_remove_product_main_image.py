# Generated by Django 3.2.9 on 2021-11-24 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_product_main_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='main_image',
        ),
    ]
