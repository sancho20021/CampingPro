# Generated by Django 2.2.4 on 2019-08-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]