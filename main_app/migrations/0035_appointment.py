# Generated by Django 4.0.4 on 2022-06-09 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0034_delete_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('service', models.CharField(choices=[('PERFECT DAYS', 'Perfect Days'), ('ROYAL STONE', 'Royal Stone'), ('CLASSIC TREATMENT', 'Classic Treatment'), ('GROWTH FACTOR FACIAL', 'Growth Factor Facial'), ('VITAMIN C', 'Vitamin C'), ('DIAMOND BRIGHTENING FACIAL', 'Diamond Brightening Facial'), ('POWER GLO FACIAL', 'Power Glo Facial'), ('PINK HIMALAYAN SALT STONE MASSAGE', 'Pink Himalayan Salt Stone Massage'), ('PRENATAL MASSAGE', 'Prenatal Massage'), ('REFLEXOLOGY', 'Reflexology'), ('DEEP TISSUE MASSAGE', 'Deep Tissue Massage')], max_length=34)),
                ('email', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=15)),
                ('date', models.DateField()),
            ],
        ),
    ]
