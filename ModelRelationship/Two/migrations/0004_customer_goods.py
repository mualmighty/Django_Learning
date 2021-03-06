# Generated by Django 2.2 on 2020-10-14 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0003_auto_20201014_0349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=16)),
                ('g_customer', models.ManyToManyField(to='Two.Customer')),
            ],
        ),
    ]
