# Generated by Django 2.2 on 2019-04-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='type',
            field=models.CharField(choices=[('hd', 'HD'), ('micro', 'Micro')], default='hd', max_length=20),
        ),
    ]