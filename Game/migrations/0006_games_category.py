# Generated by Django 3.2.7 on 2021-11-02 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Game.category'),
        ),
    ]
