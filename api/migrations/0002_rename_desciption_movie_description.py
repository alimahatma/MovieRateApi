# Generated by Django 4.0.5 on 2022-06-10 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='desciption',
            new_name='description',
        ),
    ]
