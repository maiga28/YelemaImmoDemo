# Generated by Django 4.2.6 on 2024-04-04 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_customuser_cover_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cover_picture',
            field=models.ImageField(blank=True, upload_to='cover_picture/'),
        ),
    ]
