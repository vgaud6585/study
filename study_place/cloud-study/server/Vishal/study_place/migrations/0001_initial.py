# Generated by Django 5.1.4 on 2025-03-23 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudyRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_head', models.CharField(max_length=100)),
                ('usr_heading', models.CharField(max_length=100)),
                ('usr_description', models.CharField(max_length=100)),
                ('usr_code_box', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_age', models.IntegerField()),
                ('usr_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
