# Generated by Django 4.0.4 on 2022-06-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('categories', '0003_remove_category_site_category_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='site',
            field=models.ForeignKey(default=1, on_delete=models.SET(1), to='sites.site'),
        ),
    ]
