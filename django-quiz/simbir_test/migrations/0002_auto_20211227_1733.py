# Generated by Django 3.2.9 on 2021-12-27 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simbir_test', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='text',
            new_name='answer_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='label',
            new_name='question_text',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='name',
            new_name='quiz_text',
        ),
    ]
