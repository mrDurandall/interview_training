# Generated by Django 4.0.4 on 2022-06-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='site',
            field=models.ManyToManyField(to='sites.site'),
        ),
    ]
