# Generated by Django 4.0.6 on 2022-08-04 17:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_alter_location_farm_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='farm_location',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), size=2), size=None),
        ),
    ]
