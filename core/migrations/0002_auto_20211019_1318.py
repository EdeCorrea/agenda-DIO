# Generated by Django 3.2.8 on 2021-10-19 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='creation_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='event_date',
            field=models.DateTimeField(verbose_name='Data do evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]