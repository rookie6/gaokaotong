# Generated by Django 2.0.10 on 2019-05-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0002_auto_20190512_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linespecialty',
            name='average',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='平均分'),
        ),
        migrations.AlterField(
            model_name='linespecialty',
            name='batch',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='批次'),
        ),
        migrations.AlterField(
            model_name='linespecialty',
            name='dual_class',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='双一流'),
        ),
        migrations.AlterField(
            model_name='linespecialty',
            name='dual_class_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='双一流名称'),
        ),
        migrations.AlterField(
            model_name='linespecialty',
            name='f211',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='211'),
        ),
        migrations.AlterField(
            model_name='linespecialty',
            name='f985',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='985'),
        ),
        migrations.AlterField(
            model_name='linespecialty',
            name='local_province_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='招生省份'),
        ),
        migrations.AlterField(
            model_name='linespecialty',
            name='max_score',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='最高分'),
        ),
        migrations.AlterField(
            model_name='linespecialty',
            name='min_score',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='最低分'),
        ),
        migrations.AlterField(
            model_name='linespecialty',
            name='proscore',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='省控线'),
        ),
        migrations.AlterField(
            model_name='linespecialty',
            name='school_type',
            field=models.CharField(max_length=30, null=True, verbose_name='办学类型'),
        ),
        migrations.AlterField(
            model_name='linespecialty',
            name='type',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='文理科'),
        ),
        migrations.AlterField(
            model_name='linespecialty',
            name='type_name',
            field=models.CharField(max_length=30, null=True, verbose_name='院校类型'),
        ),
        migrations.AlterField(
            model_name='linespecialty',
            name='year',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='年份'),
        ),
    ]
