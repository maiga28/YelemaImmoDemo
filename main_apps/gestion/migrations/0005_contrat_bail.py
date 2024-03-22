# Generated by Django 4.2.6 on 2023-11-29 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_proprietaire_image_alter_propriete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrat_bail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debut', models.DateTimeField(auto_now_add=True)),
                ('fin', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('propriete', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.propriete')),
            ],
        ),
    ]