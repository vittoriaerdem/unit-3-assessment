# Generated by Django 2.2.3 on 2019-09-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='DEFAULT VALUE', max_length=56)),
                ('country', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('arrived', models.CharField(default='DEFAULT VALUE', max_length=10)),
                ('departed', models.CharField(default='DEFAULT VALUE', max_length=10)),
            ],
        ),
    ]
