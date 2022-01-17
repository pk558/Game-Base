# Generated by Django 3.2.7 on 2021-11-02 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0018_auto_20211102_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Platform',
                'verbose_name_plural': 'Platforms',
            },
        ),
        migrations.AddField(
            model_name='games',
            name='platform',
            field=models.ManyToManyField(to='Game.Platform'),
        ),
    ]