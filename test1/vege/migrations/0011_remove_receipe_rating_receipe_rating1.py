# Generated by Django 5.1 on 2024-09-27 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0010_remove_receipe_rating_2_receipe_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipe',
            name='rating',
        ),
        migrations.AddField(
            model_name='receipe',
            name='rating1',
            field=models.IntegerField(blank=True, db_column='rating', default=0, null=True),
        ),
    ]
