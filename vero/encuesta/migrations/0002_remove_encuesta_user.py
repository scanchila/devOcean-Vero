# Generated by Django 3.2.7 on 2021-10-25 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encuesta',
            name='user',
        ),
    ]
