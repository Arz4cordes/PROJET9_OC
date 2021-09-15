# Generated by Django 3.2.7 on 2021-09-09 11:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookViewpoints', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='ticket_ref',
            new_name='ticket',
        ),
        migrations.RemoveField(
            model_name='review',
            name='Rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='review',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_date',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='user_name',
        ),
        migrations.AddField(
            model_name='review',
            name='body',
            field=models.TextField(blank=True, max_length=8192),
        ),
        migrations.AddField(
            model_name='review',
            name='headline',
            field=models.CharField(default='Titre de la critique', max_length=128),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='review',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='title',
            field=models.CharField(default='Titre du ticket', max_length=128),
        ),
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='img_url',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(blank=True, max_length=2048),
        ),
    ]
