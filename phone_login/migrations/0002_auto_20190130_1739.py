# Generated by Django 2.1.5 on 2019-01-30 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone_login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
