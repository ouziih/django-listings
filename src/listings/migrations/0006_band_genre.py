# Generated by Django 5.0.4 on 2024-04-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_delete_client_delete_panier_delete_vettements_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock')], default='SP', max_length=10),
            preserve_default=False,
        ),
    ]
