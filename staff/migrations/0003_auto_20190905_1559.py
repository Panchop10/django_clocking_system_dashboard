# Generated by Django 2.2.5 on 2019-09-05 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_employees_timeclocks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='working',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='timeclocks',
            name='clock_status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='timeclocks',
            name='sent',
            field=models.IntegerField(),
        ),
    ]
