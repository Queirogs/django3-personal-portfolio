# Generated by Django 4.0 on 2022-02-25 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
    ]
