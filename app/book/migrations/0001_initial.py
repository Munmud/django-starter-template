# Generated by Django 5.0.1 on 2024-02-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('price', models.FloatField()),
            ],
        ),
    ]
