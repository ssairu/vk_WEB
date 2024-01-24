# Generated by Django 4.2.7 on 2024-01-23 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='like',
            constraint=models.UniqueConstraint(fields=('user', 'content_type', 'object_id'), name='single like'),
        ),
    ]