# Generated by Django 3.2.7 on 2021-11-02 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0002_rename_discription_game_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': 'Game', 'verbose_name_plural': 'Games'},
        ),
    ]