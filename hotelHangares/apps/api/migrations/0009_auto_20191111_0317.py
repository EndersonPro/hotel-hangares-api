# Generated by Django 2.2.5 on 2019-11-11 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20191105_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='tipoHabitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tipo', to='api.TipoHabitacion'),
        ),
    ]
