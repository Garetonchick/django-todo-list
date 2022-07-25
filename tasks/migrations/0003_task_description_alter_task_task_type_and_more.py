# Generated by Django 4.0.6 on 2022-07-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_task_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(max_length=66),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=144),
        ),
    ]
