# Generated by Django 4.2.9 on 2024-08-03 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imageUrl',
            field=models.CharField(max_length=500000),
        ),
    ]
