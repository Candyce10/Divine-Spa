# Generated by Django 4.0.4 on 2022-06-07 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]
