# Generated by Django 3.1.2 on 2020-10-16 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20201016_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
