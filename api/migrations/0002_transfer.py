# Generated by Django 2.2.12 on 2021-01-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentfrom', models.CharField(max_length=244)),
                ('sendto', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=100)),
            ],
        ),
    ]
