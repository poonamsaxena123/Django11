# Generated by Django 5.1 on 2024-09-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0009_remove_receipe_rating_receipe_rating_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipe',
            name='rating_2',
        ),
        migrations.AddField(
            model_name='receipe',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]