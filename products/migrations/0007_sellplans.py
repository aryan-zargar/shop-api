# Generated by Django 4.2.9 on 2024-08-12 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='sellPlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromMonth', models.IntegerField()),
                ('toMonth', models.IntegerField()),
            ],
        ),
    ]
