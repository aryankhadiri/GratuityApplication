# Generated by Django 3.0.3 on 2020-04-18 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('time_frame', models.CharField(max_length=2)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.Employee')),
            ],
        ),
    ]
