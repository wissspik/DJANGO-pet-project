# Generated by Django 5.1.4 on 2025-02-01 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0003_rename_user_id_url_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='url_id',
            new_name='url',
        ),
    ]
