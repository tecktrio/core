# Generated by Django 4.2.2 on 2023-06-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Recovery_Email', models.CharField(max_length=50)),
                ('Contact_Number', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Street', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('Address_1', models.CharField(max_length=50)),
                ('Address_2', models.CharField(max_length=50)),
                ('Address_3', models.CharField(max_length=50)),
            ],
        ),
    ]
