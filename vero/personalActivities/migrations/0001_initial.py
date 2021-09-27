# Generated by Django 3.2.7 on 2021-09-27 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalActivites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('imageURL', models.CharField(max_length=255)),
                ('videoURL', models.CharField(max_length=255)),
                ('lecture', models.CharField(max_length=255)),
                ('pub_data', models.DateTimeField(verbose_name='date published')),
                ('duration', models.DurationField(max_length=255)),
                ('activityType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalActivities.activitytype')),
            ],
        ),
    ]
