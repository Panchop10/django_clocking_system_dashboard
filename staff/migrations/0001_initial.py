# Generated by Django 2.2.5 on 2019-09-05 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=255)),
            ],
        ),
    ]
