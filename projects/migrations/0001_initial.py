# Generated by Django 4.0.5 on 2022-06-06 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('project_shot_des', models.TextField()),
                ('slot1_900x800px', models.FileField(upload_to='project_images/')),
                ('slot2_900x800px', models.FileField(upload_to='project_images/')),
                ('slot3_900x800px', models.FileField(upload_to='project_images/')),
                ('about_project', models.TextField()),
                ('date', models.DateField()),
                ('client_name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=255, null=True)),
                ('banner_img_2400x1640px', models.FileField(upload_to='project_images/')),
                ('Left_up_image_960x640px', models.FileField(upload_to='project_images/')),
                ('left_down_image_960x640px', models.FileField(upload_to='project_images/')),
                ('right_up_image_960x640px', models.FileField(upload_to='project_images/')),
                ('right_down_image_960x640px', models.FileField(upload_to='project_images/')),
            ],
        ),
    ]
