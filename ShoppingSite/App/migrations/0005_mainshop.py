# Generated by Django 2.2 on 2020-11-03 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_mainmustbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=512)),
                ('name', models.CharField(max_length=64)),
                ('trackid', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'aaa_shop',
            },
        ),
    ]