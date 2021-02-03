# Generated by Django 2.2.12 on 2021-01-29 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210124_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gorilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]