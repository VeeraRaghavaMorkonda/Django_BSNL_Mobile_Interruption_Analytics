# Generated by Django 2.1.7 on 2019-10-09 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interruption_analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interruptions_table',
            name='DURATION',
            field=models.FloatField(),
        ),
    ]
