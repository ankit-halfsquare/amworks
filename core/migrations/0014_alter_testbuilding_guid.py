# Generated by Django 3.2 on 2022-08-31 09:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_testbuildingitem_guid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testbuilding',
            name='guid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True),
        ),
    ]
