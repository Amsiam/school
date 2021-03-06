# Generated by Django 3.1.4 on 2020-12-29 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='নাম')),
                ('no', models.IntegerField(verbose_name='নাম্বার')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='নাম')),
                ('roll', models.IntegerField(verbose_name='রোল')),
                ('id_no', models.IntegerField(verbose_name='আইডি')),
                ('image', models.FileField(upload_to='uploads/', verbose_name='ছবি')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.class', verbose_name='শ্রেণি')),
            ],
        ),
    ]
