# Generated by Django 4.0.3 on 2022-06-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourclint', '0002_alter_clint_compny_logo_comapany_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clint_compny_logo',
            name='Comapany_logo',
            field=models.ImageField(height_field=80, upload_to='brands/', width_field=272),
        ),
    ]
