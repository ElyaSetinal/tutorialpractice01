# Generated by Django 4.0.3 on 2023-07-06 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='votes',
            field=models.IntegerField(null=True, verbose_name='투표수'),
        ),
    ]
