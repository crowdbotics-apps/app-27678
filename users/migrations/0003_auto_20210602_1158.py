# Generated by Django 2.2.20 on 2021-06-02 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210602_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='emailid',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
