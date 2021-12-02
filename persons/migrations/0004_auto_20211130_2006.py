# Generated by Django 3.2.9 on 2021-12-01 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20211130_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='fri',
            new_name='day1',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='mon',
            new_name='day10',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='sat',
            new_name='day11',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='sun',
            new_name='day12',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='thu',
            new_name='day13',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='tue',
            new_name='day14',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='wed',
            new_name='day15',
        ),
        migrations.AddField(
            model_name='schedule',
            name='day2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='schedule',
            name='day3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='schedule',
            name='day4',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='schedule',
            name='day5',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='schedule',
            name='day6',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='schedule',
            name='day7',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='schedule',
            name='day8',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='schedule',
            name='day9',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='schedule',
            name='employee',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='persons.employee'),
        ),
    ]
