# Generated by Django 5.1 on 2024-09-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0007_remove_receipe_rating2_receipe_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='rating',
            field=models.IntegerField(blank=True, db_column='new_rating', default=0, null=True),
        ),
    ]
