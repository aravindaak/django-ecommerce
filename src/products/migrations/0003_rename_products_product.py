# Generated by Django 3.2.6 on 2021-08-24 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
