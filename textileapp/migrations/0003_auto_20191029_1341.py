# Generated by Django 2.2.4 on 2019-10-29 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textileapp', '0002_auto_20191029_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buynow',
            old_name='state1',
            new_name='state',
        ),
    ]
