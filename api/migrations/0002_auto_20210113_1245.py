# Generated by Django 3.1.5 on 2021-01-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
