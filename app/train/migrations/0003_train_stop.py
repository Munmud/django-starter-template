# Generated by Django 5.0.1 on 2024-02-09 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0002_station'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('train_id', models.IntegerField(primary_key=True, serialize=False)),
                ('train_name', models.CharField(max_length=255)),
                ('capacity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.CharField(max_length=50)),
                ('departure_time', models.CharField(max_length=50)),
                ('fare', models.PositiveIntegerField()),
                ('station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.station')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stops', to='train.train')),
            ],
        ),
    ]
