# Generated by Django 3.1.1 on 2020-10-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostapi', '0003_auto_20201001_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roastboastmodel',
            name='choices',
            field=models.BooleanField(choices=[('Boast', True), (False, 'Roast')], default=True),
        ),
    ]