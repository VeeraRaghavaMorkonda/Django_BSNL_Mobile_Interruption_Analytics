# Generated by Django 2.1.7 on 2019-10-10 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0011_auto_20191010_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nsn3g_table',
            name='DATE',
            field=models.DateField(),
        ),
    ]
