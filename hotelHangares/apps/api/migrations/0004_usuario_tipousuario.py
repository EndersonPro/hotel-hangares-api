# Generated by Django 2.2.5 on 2019-11-02 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_usuario_tipousuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipoUsuario',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, to='api.TipoUsuario'),
        ),
    ]