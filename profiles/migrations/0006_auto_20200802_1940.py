# Generated by Django 3.0.8 on 2020-08-02 17:40

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20200802_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseekerprofile',
            name='coding_languages',
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='coding_languages',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('JavaScript', 'JavaScript'), ('Python', 'Python'), ('Java', 'Java'), ('PHP', 'PHP'), ('C#', 'C#'), ('C++', 'C++'), ('TypeScript', 'TypeScript'), ('Shell', 'Shell'), ('C', 'C'), ('Ruby', 'Ruby'), ('Other', 'Other')], max_length=63),
        ),
        migrations.RemoveField(
            model_name='jobseekerprofile',
            name='languages',
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('English', 'English'), ('Mandarin Chinese', 'Mandarin Chinese'), ('Hindi', 'Hindi'), ('Spanish', 'Spanish'), ('French', 'French'), ('Arabic', 'Arabic'), ('Bengali', 'Bengali'), ('Russian', 'Russian'), ('Portuguese', 'Portuguese'), ('Indonesian', 'Indonesian'), ('Other', 'Other')], max_length=96),
        ),
        migrations.DeleteModel(
            name='CodingLanguages',
        ),
        migrations.DeleteModel(
            name='Languages',
        ),
    ]