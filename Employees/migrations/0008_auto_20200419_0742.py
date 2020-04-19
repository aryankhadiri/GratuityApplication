# Generated by Django 3.0.3 on 2020-04-19 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0007_auto_20200419_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='paid_today',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tip',
            name='time_frame',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=20),
        ),
    ]