
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models

import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(db_index=True, default=True, help_text='状态', verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('bank_id', shortuuidfield.fields.ShortUUIDField(blank=True, db_index=True, editable=False, help_text='题库唯一标识', max_length=22, null=True)),
                ('choice_num', models.IntegerField(default=0, help_text='选择题数', verbose_name='选择题数')),
                ('fillinblank_num', models.IntegerField(default=0, help_text='填空题数', verbose_name='填空题数')),
                ('bank_type', models.IntegerField(choices=[(0, '技术类'), (1, '教育类'), (2, '文化类'), (3, '常识类'), (4, '心理类')], default=0, help_text='题库类型', verbose_name='题库类型')),
                ('kind_num', models.IntegerField(default=0, help_text='问卷使用次数', verbose_name='问卷使用次数')),
                ('partin_num', models.IntegerField(default=0, help_text='总答题人数', verbose_name='总答题人数')),
            ],
            options={
                'verbose_name': '题库',
                'verbose_name_plural': '题库',
            },
        ),
        migrations.CreateModel(
            name='ChoiceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(db_index=True, default=True, help_text='状态', verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('image_url', models.CharField(blank=True, help_text='题目图片', max_length=255, null=True, verbose_name='图片链接')),
                ('audio_url', models.CharField(blank=True, help_text='题目音频', max_length=255, null=True, verbose_name='音频链接')),
                ('audio_time', models.IntegerField(default=0, help_text='题目音频时长', verbose_name='音频时长')),
                ('bank_id', models.CharField(blank=True, db_index=True, help_text='题库唯一标识', max_length=32, null=True, verbose_name='题库id')),
                ('ctype', models.IntegerField(choices=[(1, '文本'), (2, '图片'), (3, '音频')], default=1, help_text='题目类型', verbose_name='题目类型')),
                ('question', models.CharField(blank=True, help_text='题目', max_length=255, null=True, verbose_name='问题')),
                ('answer', models.CharField(blank=True, help_text='答案', max_length=255, null=True, verbose_name='答案')),
                ('item1', models.CharField(blank=True, help_text='选项一', max_length=255, null=True, verbose_name='选项1')),
                ('item2', models.CharField(blank=True, help_text='选项二', max_length=255, null=True, verbose_name='选项2')),
                ('item3', models.CharField(blank=True, help_text='选项三', max_length=255, null=True, verbose_name='选项3')),
                ('item4', models.CharField(blank=True, help_text='选项四', max_length=255, null=True, verbose_name='选项4')),
                ('item5', models.CharField(blank=True, help_text='选项五', max_length=255, null=True, verbose_name='选项5')),
                ('source', models.CharField(blank=True, help_text='出处', max_length=255, null=True, verbose_name='出处')),
            ],
            options={
                'verbose_name': '选择题',
                'verbose_name_plural': '选择题',
            },
        ),
        migrations.CreateModel(
            name='CompetitionKindInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(db_index=True, default=True, help_text='状态', verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('kind_id', shortuuidfield.fields.ShortUUIDField(blank=True, db_index=True, editable=False, help_text='问卷类别唯一标识', max_length=22, null=True)),
                ('account_id', models.CharField(blank=True, db_index=True, help_text='商家账户唯一标识', max_length=32, null=True, verbose_name='出题账户id')),
                ('app_id', models.CharField(blank=True, db_index=True, help_text='应用唯一标识', max_length=32, null=True, verbose_name='应用id')),
                ('bank_id', models.CharField(blank=True, db_index=True, help_text='题库唯一标识', max_length=32, null=True, verbose_name='题库id')),
                ('kind_type', models.IntegerField(choices=[(0, '技术类'), (1, '教育类'), (2, '文化类'), (3, '常识类'), (6, '地理类'), (7, '体育类'), (4, '心理类')], default=0, help_text='问卷类型', verbose_name='问卷类型')),
                ('kind_name', models.CharField(blank=True, help_text='竞赛类别名称', max_length=32, null=True, verbose_name='问卷名称')),
                ('sponsor_name', models.CharField(blank=True, help_text='赞助商名称', max_length=60, null=True, verbose_name='赞助商名称')),
                ('total_score', models.IntegerField(default=0, help_text='总分数', verbose_name='总分数')),
                ('question_num', models.IntegerField(default=0, help_text='出题数量', verbose_name='题目个数')),
                ('cop_startat', models.DateTimeField(default=django.utils.timezone.now, help_text='问卷开始时间', verbose_name='问卷开始时间')),
                ('period_time', models.IntegerField(default=60, help_text='答题时间(min)', verbose_name='答题时间')),
                ('cop_finishat', models.DateTimeField(blank=True, help_text='问卷结束时间', null=True, verbose_name='问卷结束时间')),
                ('total_partin_num', models.IntegerField(default=0, help_text='总参与人数', verbose_name='total_partin_num')),
            ],
            options={
                'verbose_name': '问卷类别信息',
                'verbose_name_plural': '问卷类别信息',
            },
        ),
        migrations.CreateModel(
            name='CompetitionQAInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(db_index=True, default=True, help_text='状态', verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('kind_id', models.CharField(blank=True, db_index=True, help_text='问卷类别唯一标识', max_length=32, null=True, verbose_name='问卷id')),
                ('qa_id', shortuuidfield.fields.ShortUUIDField(blank=True, db_index=True, editable=False, help_text='QA 唯一标识', max_length=22, null=True)),
                ('uid', models.CharField(blank=True, db_index=True, help_text='用户唯一标识', max_length=32, null=True, verbose_name='用户id')),
                ('qsrecord', models.TextField(blank=True, help_text='问题记录', max_length=10000, null=True, verbose_name='问题记录')),
                ('asrecord', models.TextField(blank=True, help_text='答案记录', max_length=10000, null=True, verbose_name='答案记录')),
                ('aslogrecord', models.TextField(blank=True, help_text='答案提交记录', max_length=10000, null=True, verbose_name='答案提交记录')),
                ('started_stamp', models.BigIntegerField(default=0, help_text='开始时间戳(毫秒)', verbose_name='开始时间戳')),
                ('finished_stamp', models.BigIntegerField(default=0, help_text='结束时间戳(毫秒)', verbose_name='结束时间戳')),
                ('expend_time', models.IntegerField(default=0, help_text='耗费时间(毫秒)', verbose_name='耗时')),
                ('started', models.BooleanField(db_index=True, default=False, help_text='是否开始', verbose_name='已开始')),
                ('finished', models.BooleanField(db_index=True, default=False, help_text='是否结束', verbose_name='已结束')),
                ('correct_num', models.IntegerField(default=0, help_text='答对数量', verbose_name='正确数')),
                ('incorrect_num', models.IntegerField(default=0, help_text='答错数量', verbose_name='错误数')),
                ('total_num', models.IntegerField(default=0, help_text='总共数量', verbose_name='总数')),
                ('score', models.IntegerField(default=0, help_text='分数', verbose_name='得分')),
            ],
            options={
                'verbose_name': '问卷问题记录',
                'verbose_name_plural': '问卷问题记录',
            },
        ),
        migrations.CreateModel(
            name='FillInBlankInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(db_index=True, default=True, help_text='状态', verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('image_url', models.CharField(blank=True, help_text='题目图片', max_length=255, null=True, verbose_name='图片链接')),
                ('audio_url', models.CharField(blank=True, help_text='题目音频', max_length=255, null=True, verbose_name='音频链接')),
                ('audio_time', models.IntegerField(default=0, help_text='题目音频时长', verbose_name='音频时长')),
                ('bank_id', models.CharField(blank=True, db_index=True, help_text='题库唯一标识', max_length=32, null=True, verbose_name='题库id')),
                ('ctype', models.IntegerField(choices=[(1, '文本'), (2, '图片'), (3, '音频')], default=1, help_text='题目类型', verbose_name='题目类型')),
                ('question', models.CharField(blank=True, help_text='题目', max_length=255, null=True, verbose_name='问题')),
                ('answer', models.CharField(blank=True, help_text='答案', max_length=255, null=True, verbose_name='答案')),
                ('source', models.CharField(blank=True, help_text='出处', max_length=255, null=True, verbose_name='出处')),
            ],
            options={
                'verbose_name': '填空题',
                'verbose_name_plural': '填空题',
            },
        ),
    ]
