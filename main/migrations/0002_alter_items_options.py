# Generated by Django 3.2.4 on 2021-07-16 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'permissions': [('can_seach', 'can do search and filtering')]},
        ),
    ]