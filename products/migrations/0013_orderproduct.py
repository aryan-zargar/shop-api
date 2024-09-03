# Generated by Django 4.2.9 on 2024-08-17 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_order_date_order_isended_alter_order_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.order')),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
