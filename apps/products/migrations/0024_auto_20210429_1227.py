# Generated by Django 2.2 on 2021-04-29 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20210427_1154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-id',)},
        ),
    ]