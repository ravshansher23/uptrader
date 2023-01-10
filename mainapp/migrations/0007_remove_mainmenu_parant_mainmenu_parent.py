# Generated by Django 4.1.4 on 2023-01-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0006_alter_mainmenu_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mainmenu",
            name="parant",
        ),
        migrations.AddField(
            model_name="mainmenu",
            name="parent",
            field=models.CharField(default=None, max_length=100, verbose_name="parent"),
        ),
    ]
