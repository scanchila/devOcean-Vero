# Generated by Django 3.2.7 on 2021-10-13 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalActivities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.CharField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='description',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='name',
            field=models.CharField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='personalactivites',
            name='description',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='personalactivites',
            name='duration',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='personalactivites',
            name='imageURL',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='personalactivites',
            name='lecture',
            field=models.CharField(blank=True, max_length=1000000),
        ),
        migrations.AlterField(
            model_name='personalactivites',
            name='name',
            field=models.CharField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='personalactivites',
            name='videoURL',
            field=models.URLField(blank=True, max_length=1000),
        ),
    ]
