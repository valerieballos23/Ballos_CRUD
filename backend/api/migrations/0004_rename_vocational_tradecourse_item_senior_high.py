# Generated by Django 4.2.13 on 2024-07-18 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_item_brgy_item_citizenship_item_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='vocational_tradecourse',
            new_name='senior_high',
        ),
    ]