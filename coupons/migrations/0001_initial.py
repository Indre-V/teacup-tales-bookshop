# Generated by Django 4.2 on 2024-09-23 11:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('discount_type', models.CharField(choices=[('percentage', 'Percentage'), ('amount', 'Amount')], max_length=10)),
                ('discount_value', models.DecimalField(decimal_places=2, help_text='Percentage value (0 to 100) or fixed amount', max_digits=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('active', models.BooleanField(default=True)),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
    ]
