# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-28 04:52
from __future__ import unicode_literals

from django.db import migrations, models

import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppConfigInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(db_index=True, default=True, help_text='状态', verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('app_id', models.CharField(db_index=True, help_text='应用唯一标识', max_length=32, verbose_name='应用id')),
                ('app_name', models.CharField(blank=True, help_text='应用名', max_length=40, null=True, verbose_name='应用名')),
                ('rule_text', models.TextField(blank=True, help_text='问卷规则', max_length=255, null=True, verbose_name='问卷规则')),
                ('is_show_userinfo', models.BooleanField(default=False, help_text='是否展示用户信息表单', verbose_name='展示用户表单')),
                ('userinfo_fields', models.CharField(blank=True, help_text='需要用户填写的字段#隔开', max_length=128, null=True, verbose_name='用户表单字段')),
                ('userinfo_field_names', models.CharField(blank=True, help_text='用户需要填写的表单字段label名称', max_length=128, null=True, verbose_name='用户表单label')),
                ('option_fields', models.CharField(blank=True, help_text='下拉框字段选项配置，#号隔开，每个字段由:h和，号组成。 如 option1:吃饭，喝水，睡觉#option2:上班，学习，看电影', max_length=128, null=True, verbose_name='下拉框字段')),
            ],
            options={
                'verbose_name': '应用配置信息',
                'verbose_name_plural': '应用配置信息',
            },
        ),
        migrations.CreateModel(
            name='BusinessAccountInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(db_index=True, default=True, help_text='状态', verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('account_id', shortuuidfield.fields.ShortUUIDField(blank=True, db_index=True, editable=False, help_text='出题账户唯一标识', max_length=22)),
                ('email', models.CharField(blank=True, db_index=True, help_text='邮箱', max_length=40, null=True, unique=True, verbose_name='邮箱')),
                ('company_name', models.CharField(blank=True, help_text='公司名称', max_length=60, null=True, verbose_name='公司名称')),
                ('company_description', models.TextField(blank=True, help_text='公司描述', null=True, verbose_name='公司描述')),
                ('company_username', models.CharField(blank=True, help_text='公司联系人', max_length=32, null=True, verbose_name='联系人')),
                ('company_phone', models.CharField(blank=True, db_index=True, help_text='公司联系电话', max_length=16, null=True, verbose_name='联系电话')),
                ('company_location', models.TextField(blank=True, help_text='公司联系地址', null=True, verbose_name='公司位置')),
            ],
            options={
                'verbose_name': '出题账户',
                'verbose_name_plural': '出题账户',
            },
        ),
        migrations.CreateModel(
            name='BusinessAppInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(db_index=True, default=True, help_text='状态', verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('account_id', models.CharField(db_index=True, help_text='出题账户唯一标识', max_length=32, verbose_name='出题账户id')),
                ('app_id', shortuuidfield.fields.ShortUUIDField(blank=True, db_index=True, editable=False, help_text='应用唯一标识', max_length=22)),
                ('app_name', models.CharField(blank=True, help_text='应用名', max_length=40, null=True, verbose_name='应用名')),
                ('app_description', models.TextField(blank=True, help_text='应用描述', null=True, verbose_name='应用描述')),
            ],
            options={
                'verbose_name': '应用信息',
                'verbose_name_plural': '应用信息',
            },
        ),
        migrations.CreateModel(
            name='UserInfoImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(db_index=True, default=True, help_text='状态', verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('uii_name', models.CharField(blank=True, help_text='信息图片配置名称', max_length=32, null=True, verbose_name='配置名称')),
                ('name', models.CharField(blank=True, help_text='姓名', max_length=60, null=True, verbose_name='姓名')),
                ('sex', models.CharField(blank=True, help_text='性别', max_length=60, null=True, verbose_name='性别')),
                ('age', models.CharField(blank=True, help_text='年龄', max_length=60, null=True, verbose_name='年龄')),
                ('phone', models.CharField(blank=True, help_text='电话', max_length=60, null=True, verbose_name='手机号')),
                ('wxid', models.CharField(blank=True, help_text='微信号', max_length=60, null=True, verbose_name='微信号')),
                ('email', models.CharField(blank=True, help_text='邮箱', max_length=60, null=True, verbose_name='邮箱')),
                ('pid', models.CharField(blank=True, help_text='身份证号', max_length=60, null=True, verbose_name='身份证号')),
                ('graduated_from', models.CharField(blank=True, help_text='毕业院校', max_length=60, null=True, verbose_name='毕业院校')),
                ('address', models.CharField(blank=True, help_text='联系地址', max_length=60, null=True, verbose_name='地址')),
            ],
            options={
                'verbose_name': '用户信息图片配置',
                'verbose_name_plural': '用户信息图片配置',
            },
        ),
        migrations.CreateModel(
            name='UserInfoRegex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(db_index=True, default=True, help_text='状态', verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('field_name', models.CharField(blank=True, help_text='字段名', max_length=16, null=True, verbose_name='字段名')),
                ('regex', models.CharField(blank=True, help_text='正则表达式', max_length=40, null=True, verbose_name='正则表达式值')),
                ('description', models.CharField(blank=True, help_text='错误描述', max_length=40, verbose_name='description')),
            ],
            options={
                'verbose_name': '用户信息字段正则表达式',
                'verbose_name_plural': '用户信息字段正则表达式',
            },
        ),
    ]
