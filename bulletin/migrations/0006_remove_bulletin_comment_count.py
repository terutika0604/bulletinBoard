# Generated by Django 4.0.6 on 2022-09-14 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0005_alter_comment_bulletin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulletin',
            name='comment_count',
        ),
    ]