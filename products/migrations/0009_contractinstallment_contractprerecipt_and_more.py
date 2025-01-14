# Generated by Django 4.2.9 on 2024-08-14 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_sellplans_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractInstallment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DueDate', models.DateField()),
                ('ContractAmount', models.IntegerField()),
                ('ContractMainAmount', models.IntegerField()),
                ('ContractIntrestAmount', models.IntegerField()),
                ('ContractTotalAmount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContractPreRecipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RecieptDate', models.DateField()),
                ('PreReceiptAmount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InstallmentPreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FacilitiesAmount', models.IntegerField()),
                ('FacilitiesIntrest', models.IntegerField()),
                ('InstallmentAmount', models.IntegerField()),
                ('LastInstallmentAmount', models.IntegerField()),
                ('ContractInstallmentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.contractinstallment')),
                ('ContractPreReciptId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.contractprerecipt')),
            ],
        ),
    ]
