# Generated by Django 4.1.4 on 2023-01-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_remove_mainmenu_url_mainmenu_parant_mainmenu_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmenu',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
