# Generated by Django 2.2.3 on 2019-08-01 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20190801_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='kol',
            field=models.IntegerField(default=0),
        ),
    ]
