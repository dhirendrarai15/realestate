# Generated by Django 3.2.7 on 2021-09-15 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='nametype',
            new_name='hometype',
        ),
    ]
