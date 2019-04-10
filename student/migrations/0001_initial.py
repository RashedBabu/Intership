# Generated by Django 2.1.7 on 2019-04-09 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.IntegerField()),
                ('intern', models.IntegerField()),
                ('company', models.IntegerField()),
                ('city', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stu_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Posting_title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('Internship_discription', models.TextField()),
                ('Location', models.CharField(max_length=50)),
                ('job_type', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.CharField(max_length=50)),
            ],
        ),
    ]