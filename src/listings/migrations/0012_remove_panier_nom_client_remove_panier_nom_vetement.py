# Generated by Django 5.0.4 on 2024-04-22 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_alter_panier_id_client_alter_panier_id_vetement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panier',
            name='nom_client',
        ),
        migrations.RemoveField(
            model_name='panier',
            name='nom_vetement',
        ),
    ]
