# Generated by Django 3.2 on 2021-05-21 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tasks',
            new_name='Task',
        ),
    ]