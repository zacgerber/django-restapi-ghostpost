# Generated by Django 3.1.1 on 2020-10-01 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghostapi', '0002_roastboastmodel_total_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roastboastmodel',
            old_name='bost',
            new_name='body',
        ),
    ]
