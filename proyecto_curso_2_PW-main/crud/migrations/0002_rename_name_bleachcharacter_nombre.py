# Generated by Django 5.1.3 on 2024-11-16 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bleachcharacter',
            old_name='name',
            new_name='nombre',
        ),
    ]