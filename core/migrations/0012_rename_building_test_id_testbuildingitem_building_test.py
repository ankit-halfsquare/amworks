# Generated by Django 3.2 on 2022-08-30 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_testbuilding_testbuildingitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testbuildingitem',
            old_name='building_test_id',
            new_name='building_test',
        ),
    ]
