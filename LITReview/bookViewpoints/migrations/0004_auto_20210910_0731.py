# Generated by Django 3.2.7 on 2021-09-10 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookViewpoints', '0003_auto_20210909_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
