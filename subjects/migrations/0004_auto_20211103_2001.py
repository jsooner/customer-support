# Generated by Django 3.2.8 on 2021-11-03 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_alter_subjects_attatchment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='attatchment',
            field=models.FileField(blank=True, null=True, upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
