# Generated by Django 4.0.5 on 2022-06-21 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearnapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='is_finished',
            new_name='status',
        ),
    ]
