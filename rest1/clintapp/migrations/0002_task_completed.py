# Generated by Django 4.1.7 on 2023-04-19 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clintapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
