# Generated by Django 4.2.4 on 2023-08-14 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='organization',
            new_name='organization_id',
        ),
    ]