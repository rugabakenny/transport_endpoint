# Generated by Django 2.2.12 on 2021-01-24 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_transfer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Postnews',
        ),
    ]