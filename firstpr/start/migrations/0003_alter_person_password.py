# Generated by Django 5.1.4 on 2025-01-14 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0002_alter_person_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
