# Generated by Django 4.1.5 on 2023-01-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='author',
            field=models.CharField(default='', max_length=60),
        ),
    ]