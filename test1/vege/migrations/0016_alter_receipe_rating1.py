# Generated by Django 5.1 on 2024-10-03 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0015_rename_rating_receipe_rating1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='rating1',
            field=models.IntegerField(blank=True, db_column='rating1', default=0, null=True),
        ),
    ]
