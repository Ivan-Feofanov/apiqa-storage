# Generated by Django 2.2.2 on 2019-06-13 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests_storage', '0004_auto_20190530_0945'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyAttachFile',
        ),
        migrations.DeleteModel(
            name='UserAttachFile',
        ),
    ]
