# Generated by Django 2.1.5 on 2020-07-31 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20200731_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='msg',
            new_name='body',
        ),
    ]
