# Generated by Django 4.2 on 2023-05-03 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_name', models.CharField(max_length=25)),
                ('place', models.CharField(max_length=25)),
                ('company_name', models.CharField(max_length=25)),
                ('designation', models.CharField(max_length=25)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
