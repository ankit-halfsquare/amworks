# Generated by Django 3.2 on 2022-08-30 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220830_0434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testbuildingitem',
            old_name='building_test',
            new_name='building_test_id',
        ),
    ]
