# Generated by Django 4.0.4 on 2022-06-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('goods', '0005_alter_good_categories_alter_good_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='sites',
            field=models.ManyToManyField(to='sites.site'),
        ),
    ]
