# Generated by Django 3.1.3 on 2020-11-25 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0005_auto_20201125_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='Slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='Time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='Title',
            new_name='title',
        ),
    ]