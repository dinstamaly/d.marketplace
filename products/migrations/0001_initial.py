# Generated by Django 2.2 on 2019-04-02 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sellers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ImageField(blank=True, null=True, upload_to=products.models.download_media_location)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=9.99, max_digits=100, null=True)),
                ('sale_active', models.BooleanField(default=False)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, default=6.99, max_digits=100, null=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.SellerAccount')),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('hd', 'HD'), ('sd', 'SD'), ('micro', 'Micro')], default='hd', max_length=20)),
                ('height', models.CharField(blank=True, max_length=20, null=True)),
                ('width', models.CharField(blank=True, max_length=20, null=True)),
                ('media', models.ImageField(blank=True, height_field='height', null=True, upload_to=products.models.thumbnail_location, width_field='width')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(blank=True, to='products.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'My Products',
                'verbose_name_plural': 'My Products',
            },
        ),
        migrations.CreateModel(
            name='CuratedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=120)),
                ('active', models.BooleanField(default=True)),
                ('products', models.ManyToManyField(blank=True, to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
