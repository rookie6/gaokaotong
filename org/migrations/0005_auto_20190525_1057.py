# Generated by Django 2.0.10 on 2019-05-25 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0004_auto_20190512_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linespecialty',
            name='sp_name',
            field=models.CharField(max_length=50, verbose_name='专业名称'),
        ),
    ]
