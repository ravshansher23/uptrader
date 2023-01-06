# Generated by Django 4.1.4 on 2023-01-06 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_data_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainmenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('url', models.CharField(max_length=255, verbose_name='Ссылка')),
                ('position', models.PositiveIntegerField(default=1, verbose_name='Позиция')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
                'ordering': ('position',),
            },
        ),
    ]