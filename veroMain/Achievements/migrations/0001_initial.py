# Generated by Django 3.2.7 on 2021-11-11 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.IntegerField(default=0)),
                ('description', models.CharField(default='NA', max_length=400)),
                ('category', models.CharField(default='NA', max_length=50)),
                ('condition', models.CharField(default='achievement_user_create_account', max_length=50)),
            ],
        ),
    ]
