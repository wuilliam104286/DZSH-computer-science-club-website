# Generated by Django 3.0.1 on 2020-02-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20200210_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=50, verbose_name='姓名'),
        ),
    ]
