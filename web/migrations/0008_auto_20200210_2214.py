# Generated by Django 3.0.1 on 2020-02-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20200206_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(default='{{ message.user }}', max_length=50, verbose_name='姓名'),
        ),
    ]
