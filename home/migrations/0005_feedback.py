# Generated by Django 5.1.2 on 2024-10-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_contact_email_alter_contact_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('feedback', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]