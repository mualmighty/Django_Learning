# Generated by Django 2.2 on 2020-10-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0005_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=16)),
            ],
        ),
    ]