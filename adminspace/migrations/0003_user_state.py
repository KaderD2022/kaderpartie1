# Generated by Django 4.1.7 on 2023-04-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminspace', '0002_alter_service_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default='on', max_length=5),
        ),
    ]
