# Generated by Django 4.2.1 on 2023-05-09 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_aboutus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tittle',
            new_name='title',
        ),
    ]
