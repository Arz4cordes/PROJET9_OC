# Generated by Django 3.2.7 on 2021-10-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookViewpoints', '0005_alter_ticket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/photos/%Y/%m/%d'),
        ),
    ]
