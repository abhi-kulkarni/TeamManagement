# Generated by Django 4.0 on 2021-12-10 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_members', '0004_alter_teammember_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammember',
            old_name='role',
            new_name='is_admin',
        ),
    ]
