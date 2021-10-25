# Generated by Django 3.2.7 on 2021-10-23 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalActivities', '0003_auto_20211013_1336'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='activities',
            field=models.ManyToManyField(through='users.User_activity', to='personalActivities.PersonalActivites'),
        ),
        migrations.AlterField(
            model_name='user_activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user_profile'),
        ),
    ]