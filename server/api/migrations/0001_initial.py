# Generated by Django 2.1 on 2018-08-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16, verbose_name='code')),
                ('tel', models.CharField(max_length=11, verbose_name='tel')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='time')),
            ],
            options={
                'verbose_name': 'code',
                'verbose_name_plural': 'code',
            },
        ),
    ]