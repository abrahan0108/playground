# Generated by Django 2.2.6 on 2019-10-11 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='user',
            new_name='users',
        ),
    ]
