# Generated by Django 2.2.5 on 2019-09-22 00:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reclamos', '0003_reclamo_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='creado',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]