# Generated by Django 5.0.2 on 2024-03-20 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_classification'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification',
            name='comment',
            field=models.TextField(default=''),
        ),
    ]
