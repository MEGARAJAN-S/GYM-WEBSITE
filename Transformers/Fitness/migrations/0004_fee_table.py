# Generated by Django 4.2.7 on 2023-12-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fitness', '0003_alter_user_table_in_time_alter_user_table_out_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='fee_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gym_id', models.CharField(max_length=5)),
                ('Name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('pay_date', models.DateField()),
                ('end_date', models.DateField()),
                ('re_day', models.IntegerField()),
            ],
        ),
    ]
