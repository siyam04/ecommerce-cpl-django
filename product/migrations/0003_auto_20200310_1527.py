# Generated by Django 3.0.3 on 2020-03-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200309_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Pending', 'PENDING'), ('Published', 'PUBLISHED'), ('Stock Out', 'STOCK_OUT')], default='Pending', max_length=20),
        ),
    ]
