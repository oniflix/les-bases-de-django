# Generated by Django 4.1.7 on 2023-02-16 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=models.TextField(default=''),
        ),
    ]