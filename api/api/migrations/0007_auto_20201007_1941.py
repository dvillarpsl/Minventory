# Generated by Django 3.1.1 on 2020-10-08 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
