# Generated by Django 5.1.2 on 2024-10-13 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_feedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Order',
        ),
    ]