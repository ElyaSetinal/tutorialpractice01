# Generated by Django 4.0.3 on 2023-07-06 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_questions_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='votes',
            field=models.IntegerField(default=0, null=True, verbose_name='투표수'),
        ),
    ]