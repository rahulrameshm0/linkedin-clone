# Generated by Django 5.1.7 on 2025-03-12 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup_login', '0004_rename_confirm_password_user_confirm_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Confirm_password',
            new_name='confirm_password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Username',
            new_name='username',
        ),
    ]
