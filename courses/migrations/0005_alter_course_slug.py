# Generated by Django 4.2.5 on 2024-02-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
