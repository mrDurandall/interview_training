# Generated by Django 4.0.4 on 2022-06-05 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hitcount', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hitcount',
            options={'verbose_name': 'Счетчик посещения', 'verbose_name_plural': 'Счетчики'},
        ),
    ]
