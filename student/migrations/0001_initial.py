# Generated by Django 5.1.2 on 2024-11-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('age', models.PositiveBigIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'),], max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
