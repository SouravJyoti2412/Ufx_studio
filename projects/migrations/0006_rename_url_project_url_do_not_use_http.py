# Generated by Django 4.0.3 on 2022-06-10 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_project_shot_des_in_100_word'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='url',
            new_name='url_do_not_use_http',
        ),
    ]
