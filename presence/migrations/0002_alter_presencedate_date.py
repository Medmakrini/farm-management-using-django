# Generated by Django 4.0.6 on 2022-08-13 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presence', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presencedate',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
