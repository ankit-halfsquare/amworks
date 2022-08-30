# Generated by Django 3.2 on 2022-08-30 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220830_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestBuilding',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('organization_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('create_user', models.IntegerField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.IntegerField(blank=True, null=True)),
                ('obsolete', models.SmallIntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('ta1_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta2_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta3_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta4_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta5_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta6_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta7_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta8_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta9_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta10_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta11_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta12_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta13_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta14_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta15_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta16_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta17_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta18_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta19_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('ta20_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl1_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl1_list', models.IntegerField(blank=True, null=True)),
                ('sl2_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl2_list', models.IntegerField(blank=True, null=True)),
                ('sl3_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl3_list', models.IntegerField(blank=True, null=True)),
                ('sl4_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl4_list', models.IntegerField(blank=True, null=True)),
                ('sl5_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl5_list', models.IntegerField(blank=True, null=True)),
                ('sl6_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl6_list', models.IntegerField(blank=True, null=True)),
                ('sl7_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl7_list', models.IntegerField(blank=True, null=True)),
                ('sl8_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl8_list', models.IntegerField(blank=True, null=True)),
                ('sl9_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl9_list', models.IntegerField(blank=True, null=True)),
                ('sl10_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl10_list', models.IntegerField(blank=True, null=True)),
                ('sl11_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl11_list', models.IntegerField(blank=True, null=True)),
                ('sl12_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl12_list', models.IntegerField(blank=True, null=True)),
                ('sl13_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl13_list', models.IntegerField(blank=True, null=True)),
                ('sl14_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl14_list', models.IntegerField(blank=True, null=True)),
                ('sl15_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl15_list', models.IntegerField(blank=True, null=True)),
                ('sl16_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl16_list', models.IntegerField(blank=True, null=True)),
                ('sl17_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl17_list', models.IntegerField(blank=True, null=True)),
                ('sl18_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl18_list', models.IntegerField(blank=True, null=True)),
                ('sl19_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl19_list', models.IntegerField(blank=True, null=True)),
                ('sl20_alias', models.CharField(blank=True, max_length=255, null=True)),
                ('sl20_list', models.IntegerField(blank=True, null=True)),
                ('zip', models.CharField(blank=True, max_length=128, null=True)),
                ('guid', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'db_table': 'building_test',
            },
        ),
        migrations.CreateModel(
            name='TestBuildingItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('parent_building_item', models.IntegerField(blank=True, null=True)),
                ('people_id', models.IntegerField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=788, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('ta1', models.CharField(blank=True, max_length=788, null=True)),
                ('ta2', models.CharField(blank=True, max_length=788, null=True)),
                ('ta3', models.CharField(blank=True, max_length=788, null=True)),
                ('ta4', models.CharField(blank=True, max_length=788, null=True)),
                ('ta5', models.CharField(blank=True, max_length=788, null=True)),
                ('ta6', models.CharField(blank=True, max_length=788, null=True)),
                ('ta7', models.CharField(blank=True, max_length=788, null=True)),
                ('ta8', models.CharField(blank=True, max_length=788, null=True)),
                ('ta9', models.CharField(blank=True, max_length=788, null=True)),
                ('ta10', models.CharField(blank=True, max_length=788, null=True)),
                ('ta11', models.CharField(blank=True, max_length=788, null=True)),
                ('ta12', models.CharField(blank=True, max_length=788, null=True)),
                ('ta13', models.CharField(blank=True, max_length=788, null=True)),
                ('ta14', models.CharField(blank=True, max_length=788, null=True)),
                ('ta15', models.CharField(blank=True, max_length=788, null=True)),
                ('ta16', models.CharField(blank=True, max_length=788, null=True)),
                ('ta17', models.CharField(blank=True, max_length=788, null=True)),
                ('ta18', models.CharField(blank=True, max_length=788, null=True)),
                ('ta19', models.CharField(blank=True, max_length=788, null=True)),
                ('ta20', models.CharField(blank=True, max_length=788, null=True)),
                ('sl1', models.IntegerField(blank=True, null=True)),
                ('sl2', models.IntegerField(blank=True, null=True)),
                ('sl3', models.IntegerField(blank=True, null=True)),
                ('sl4', models.IntegerField(blank=True, null=True)),
                ('sl5', models.IntegerField(blank=True, null=True)),
                ('sl6', models.IntegerField(blank=True, null=True)),
                ('sl7', models.IntegerField(blank=True, null=True)),
                ('sl8', models.IntegerField(blank=True, null=True)),
                ('sl9', models.IntegerField(blank=True, null=True)),
                ('sl10', models.IntegerField(blank=True, null=True)),
                ('sl11', models.IntegerField(blank=True, null=True)),
                ('sl12', models.IntegerField(blank=True, null=True)),
                ('sl13', models.IntegerField(blank=True, null=True)),
                ('sl14', models.IntegerField(blank=True, null=True)),
                ('sl15', models.IntegerField(blank=True, null=True)),
                ('sl16', models.IntegerField(blank=True, null=True)),
                ('sl17', models.IntegerField(blank=True, null=True)),
                ('sl18', models.IntegerField(blank=True, null=True)),
                ('sl19', models.IntegerField(blank=True, null=True)),
                ('sl20', models.IntegerField(blank=True, null=True)),
                ('obsolete', models.SmallIntegerField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('create_user', models.IntegerField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.IntegerField(blank=True, null=True)),
                ('guid', models.CharField(blank=True, max_length=255, null=True)),
                ('additional_data_type_form_instance_id', models.IntegerField(blank=True, null=True)),
                ('additional_data_type_form_name', models.CharField(blank=True, max_length=255, null=True)),
                ('building_item_category_id', models.IntegerField(blank=True, null=True)),
                ('batch_id', models.CharField(blank=True, max_length=255, null=True)),
                ('building_test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.testbuilding')),
            ],
            options={
                'db_table': 'building_item_test',
            },
        ),
    ]
