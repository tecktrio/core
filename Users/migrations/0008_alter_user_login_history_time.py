# Generated by Django 4.2.2 on 2023-07-26 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_alter_user_login_history_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_login_history',
            name='Time',
            field=models.CharField(default='09:28:39', max_length=50),
        ),
    ]
