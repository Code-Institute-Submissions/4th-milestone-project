# Generated by Django 3.0.8 on 2020-08-02 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='eduction_item',
            new_name='education_item',
        ),
    ]