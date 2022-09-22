# Generated by Django 4.1 on 2022-09-22 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('estimated_end', models.DateField(default=datetime.date.today)),
                ('priority', models.IntegerField(default=3)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]