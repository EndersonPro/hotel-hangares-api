# Generated by Django 2.2.5 on 2019-11-05 13:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20191102_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipousuario',
            name='creado',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
