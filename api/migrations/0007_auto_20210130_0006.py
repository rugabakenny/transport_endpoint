# Generated by Django 2.2.12 on 2021-01-30 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_lakes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lakes',
            new_name='Lake',
        ),
    ]