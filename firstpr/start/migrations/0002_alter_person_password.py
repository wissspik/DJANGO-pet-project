# Generated by Django 5.1.4 on 2024-12-21 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(db_index=True, max_length=20),
        ),
    ]
