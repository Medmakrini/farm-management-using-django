# Generated by Django 4.0.6 on 2022-07-31 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('worker', '0002_rename_szcondname_worker_secondname'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresenceDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hoursofWork', models.TextField()),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.worker')),
            ],
        ),
    ]
