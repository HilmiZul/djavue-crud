# Generated by Django 2.2.13 on 2020-08-02 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kursus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='aktif',
            new_name='status',
        ),
    ]
