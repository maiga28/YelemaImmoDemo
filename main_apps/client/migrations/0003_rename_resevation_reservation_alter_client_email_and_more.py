# Generated by Django 4.2.6 on 2023-11-14 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_propriete_image_delete_caracteristique'),
        ('client', '0002_resevation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resevation',
            new_name='Reservation',
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
