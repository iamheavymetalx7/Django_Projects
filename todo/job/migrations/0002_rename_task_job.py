# Generated by Django 4.1.4 on 2022-12-08 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Task", new_name="Job",),
    ]