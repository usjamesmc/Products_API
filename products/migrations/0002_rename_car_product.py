# Generated by Django 4.0.4 on 2022-04-13 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Car',
            new_name='Product',
        ),
    ]
