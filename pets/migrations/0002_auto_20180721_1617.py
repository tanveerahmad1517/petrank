# Generated by Django 2.0.1 on 2018-07-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='elo_rating',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='pet',
            name='species',
            field=models.CharField(choices=[('CAT', 'Cat'), ('DOG', 'Dog')], default='DOG', max_length=16),
        ),
    ]
