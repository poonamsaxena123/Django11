# Generated by Django 5.1 on 2024-09-27 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_receipe_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipe',
            old_name='rating',
            new_name='rating1',
        ),
    ]
