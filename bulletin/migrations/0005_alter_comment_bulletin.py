# Generated by Django 4.0.6 on 2022-09-14 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0004_alter_comment_bulletin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='bulletin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletin.bulletin'),
        ),
    ]
