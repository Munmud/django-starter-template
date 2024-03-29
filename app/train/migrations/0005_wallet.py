# Generated by Django 5.0.1 on 2024-02-09 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0004_alter_stop_arrival_time_alter_stop_departure_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('wallet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('balance', models.PositiveIntegerField()),
                ('wallet_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='train.trainuser')),
            ],
        ),
    ]
