# Generated by Django 3.1.1 on 2020-10-01 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostapi', '0005_auto_20201001_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roastboastmodel',
            name='choices',
            field=models.BooleanField(choices=[(True, 'Boast'), (False, 'Roast')], default=True),
        ),
    ]
