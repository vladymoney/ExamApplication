# Generated by Django 3.0.5 on 2022-12-16 17:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]