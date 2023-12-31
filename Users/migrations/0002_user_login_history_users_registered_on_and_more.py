# Generated by Django 4.2.2 on 2023-06-22 03:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Login_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(default=None, max_length=50)),
                ('Date', models.CharField(default=datetime.date(2023, 6, 22), max_length=50)),
                ('Time', models.CharField(default='09:00:50', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='Registered_On',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='Address_1',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='Address_2',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='Address_3',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='City',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='Contact_Number',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='Country',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='Email',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='First_Name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='Last_Name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='Password',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='Recovery_Email',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='Street',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
