# Generated by Django 2.2 on 2021-02-03 14:06

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured', models.BooleanField(default=False)),
                ('best_seller', models.BooleanField(default=False)),
                ('top_rated', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=150)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('size', models.CharField(choices=[('not applicable', 'not applicable'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], default='not applicable', max_length=50)),
                ('color', models.CharField(default='not applicable', max_length=70)),
                ('quantity', models.IntegerField(default=10)),
                ('availability', models.CharField(choices=[('in_stock', 'In Stock'), ('not_available', 'Not Available')], default='in_stock', max_length=70)),
                ('warranty', models.CharField(choices=[('no_warranty', 'No Warranty'), ('local_seller_warranty', 'Local Seller Warranty'), ('brand_warranty', 'Brand Warranty')], default='no_warranty', max_length=100)),
                ('services', models.CharField(choices=[('cash_on_delivery', 'Cash On Delivery'), ('free_shipping', 'Free Shipping')], default='cash_on_delivery', max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Brand')),
                ('category', models.ManyToManyField(to='products.Category')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Collection')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
