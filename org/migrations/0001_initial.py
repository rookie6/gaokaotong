# Generated by Django 2.0.10 on 2019-05-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinePro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=30, verbose_name='省份')),
                ('type', models.CharField(blank=True, max_length=30, verbose_name='文理科')),
                ('batch', models.CharField(blank=True, max_length=30, verbose_name='批次')),
                ('year', models.CharField(blank=True, max_length=30, verbose_name='年份')),
                ('average', models.CharField(blank=True, max_length=30, verbose_name='分数')),
            ],
            options={
                'verbose_name': '省份录取分数线',
                'verbose_name_plural': '省份录取分数线',
            },
        ),
        migrations.CreateModel(
            name='SchoolInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=30, verbose_name='学校名称')),
                ('province_name', models.CharField(max_length=30, verbose_name='省份')),
                ('city_name', models.CharField(blank=True, max_length=30, verbose_name='城市名称')),
                ('county_name', models.CharField(blank=True, max_length=30, verbose_name='地区名称')),
                ('school_type', models.CharField(max_length=30, verbose_name='办学类型')),
                ('type_name', models.CharField(max_length=30, verbose_name='院校类型')),
                ('school_intro', models.TextField(blank=True, verbose_name='学校简介')),
                ('subject', models.TextField(blank=True, verbose_name='重点学科')),
                ('admissions', models.CharField(blank=True, max_length=30, verbose_name='自主招生')),
                ('central', models.CharField(blank=True, max_length=30, verbose_name='中央部委')),
                ('department', models.CharField(blank=True, max_length=30, verbose_name='教育部直属')),
                ('f211', models.CharField(blank=True, max_length=30, verbose_name='211')),
                ('f985', models.CharField(blank=True, max_length=30, verbose_name='985')),
                ('dual_class', models.CharField(blank=True, max_length=30, verbose_name='双一流')),
                ('dual_class_name', models.CharField(blank=True, max_length=30, verbose_name='双一流名称')),
            ],
            options={
                'verbose_name': '学校信息',
                'verbose_name_plural': '学校信息',
            },
        ),
        migrations.CreateModel(
            name='SpecialtyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_name', models.CharField(max_length=30, verbose_name='专业名称')),
                ('level1_name', models.CharField(max_length=30, verbose_name='专业层次')),
                ('level2_name', models.CharField(max_length=30, verbose_name='专业门类')),
                ('level3_name', models.CharField(max_length=30, verbose_name='专业名称')),
                ('limit_year', models.CharField(max_length=30, verbose_name='专业学习年份')),
                ('degree', models.CharField(max_length=30, verbose_name='授予学士')),
                ('content', models.TextField(verbose_name='专业简介')),
                ('job', models.TextField(verbose_name='发展')),
                ('is_what', models.TextField(verbose_name='是什么')),
                ('do_what', models.TextField(verbose_name='干什么')),
                ('learn_what', models.TextField(verbose_name='学习什么')),
                ('rate', models.CharField(max_length=30, verbose_name='男女比例')),
                ('sel_adv', models.CharField(max_length=30, verbose_name='生源选择')),
            ],
            options={
                'verbose_name': '专业信息',
                'verbose_name_plural': '专业信息',
            },
        ),
    ]
