# Generated by Django 3.2.4 on 2021-07-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210715_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='samples',
            name='text',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
