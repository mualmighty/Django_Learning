# Generated by Django 2.2 on 2020-10-13 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='s_token',
            field=models.CharField(default=None, max_length=256),
        ),
    ]
