# Generated by Django 3.0.6 on 2020-10-14 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201014_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(default='title', upload_to='covers/'),
        ),
    ]