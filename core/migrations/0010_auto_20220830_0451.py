# Generated by Django 3.2 on 2022-08-30 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_building_test_id_testbuildingitem_building'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testbuildingitem',
            name='building',
        ),
        migrations.DeleteModel(
            name='TestBuilding',
        ),
        migrations.DeleteModel(
            name='TestBuildingItem',
        ),
    ]