# Generated by Django 4.1.7 on 2023-03-07 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='myUser',
        ),
    ]