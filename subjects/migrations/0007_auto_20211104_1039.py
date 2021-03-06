# Generated by Django 3.2.8 on 2021-11-04 02:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0006_auto_20211104_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='body',
            field=models.TextField(blank=True, default='asdf'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subjects',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subjects',
            name='slug',
            field=models.SlugField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subjects',
            name='title',
            field=models.CharField(blank=True, default='asdf', max_length=100),
            preserve_default=False,
        ),
    ]
