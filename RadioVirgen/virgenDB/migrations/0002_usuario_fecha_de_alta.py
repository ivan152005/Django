# Generated by Django 5.1.4 on 2025-02-18 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virgenDB', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fecha_de_alta',
            field=models.DateField(default=datetime.date.today),
            preserve_default=False,
        ),
    ]
