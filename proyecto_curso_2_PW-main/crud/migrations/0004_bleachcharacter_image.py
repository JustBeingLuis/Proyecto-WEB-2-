# Generated by Django 5.1.3 on 2024-11-16 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_rename_nombre_bleachcharacter_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bleachcharacter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]