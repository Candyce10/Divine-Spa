# Generated by Django 4.0.4 on 2022-06-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_review_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=15)),
            ],
        ),
    ]