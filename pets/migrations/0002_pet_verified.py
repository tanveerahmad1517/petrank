# Generated by Django 2.0.1 on 2018-07-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
