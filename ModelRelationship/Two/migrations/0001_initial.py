# Generated by Django 2.2 on 2020-10-14 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=16)),
                ('p_age', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='IDCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_num', models.CharField(max_length=18, unique=True)),
                ('id_person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Two.Person')),
            ],
        ),
    ]
