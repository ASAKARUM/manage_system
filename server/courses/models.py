# -*- coding: utf-8 -*-

'''本文件用于构建和课程紧密相关的数据库表'''

from django.db import models


class Teacher(models.Model):
    '''保存上课教师信息的类

    :字段解释:
    + name: 老师姓名 类型为CharField, 最大长度为20
    + tel: 老师电话号码 类型为CharField, 最大长度为11
    '''
    name = models.CharField(max_length=20, blank=False)
    tel = models.CharField(max_length=11, blank=True, null=True)


def get_teacher():
    '''返回一个标记为已删除的 Teacher 行'''
    return Teacher.objects.get_or_create(name='deleted')[0]


class Courses(models.Model):
    '''保存课程信息的类

    :字段解释:
    + DATE_CHOICES: 日期选择项 (1, '星期一'), (2, '星期二'), (3, '星期三'),

                    (4, '星期四'), (5, '星期五'), (6, '星期六'), (7, '星期七')
    + name: 课程名 类型为CharField, 最大长度为20
    + teacher_id: 上课教师 类型为TimeField
    + time: 上课时间 类型为CharField max_length=20
    + date: 每周上课日期 类型为PositiveSmallIntegerField
    + time_length: 课程单时长, 类型为PositiveIntegerField, 默认为120分钟
    + total_sec: 总课节数 类型为PositiveIntegerField, 默认为0
    + price: 课程金额 类型为FloatField
    '''
    DATE_CHOICES = (
        (1, '星期一'),
        (2, '星期二'),
        (3, '星期三'),
        (4, '星期四'),
        (5, '星期五'),
        (6, '星期六'),
        (7, '星期七'),
    )

    name = models.CharField(max_length=20, blank=False)
    teacher_id = models.ForeignKey(
        Teacher,
        related_name='teacher',
        on_delete=models.SET(get_teacher)
    )
    time = models.TimeField(blank=True, null=True)
    date = models.PositiveSmallIntegerField(
        choices=DATE_CHOICES, default=0)
    time_length = models.PositiveIntegerField(default=120)
    total_sec = models.PositiveIntegerField(default=0)
    price = models.FloatField(null=True, blank=True)


class Section(models.Model):
    '''保存单个课节信息的类

    :字段解释:
    + course_id: 对应课程, 类型为外键, 对应Courses类
    + count: 对应课次数, 类型为PositiveIntegerField
    + name: 课节名 类型为CharField, 最大长度为30
    + date: 该节课上课日期, 类型为DateField
    + start_time: 该课节开始时间 类型为TimeField
    + start_time: 该课节结束时间 类型为TimeField
    + location: 上课地方 类型为CharField, 最大长度为100
    + is_cancel: 标识是否销课 类型为BooleanField, 默认为False即没有销课
    '''
    course_id = models.ForeignKey(
        Courses,
        related_name='sections',
        on_delete=models.CASCADE
    )
    count = models.PositiveIntegerField()
    name = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)
    is_cancel = models.BooleanField(default=False)
