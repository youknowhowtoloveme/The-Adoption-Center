# Generated by Django 3.2.13 on 2022-10-26 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_project', '0005_alter_pet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='url',
            field=models.CharField(default='', max_length=50),
        ),
    ]
