# Generated by Django 4.1.7 on 2023-04-07 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('receptionspace', '0004_visite_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonneeAdministrative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=3, null=True)),
                ('conjugal_status', models.CharField(max_length=15, null=True)),
                ('type_populate', models.CharField(max_length=255, null=True)),
                ('social_protection', models.CharField(max_length=255, null=True)),
                ('visite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='receptionspace.visite')),
            ],
        ),
        migrations.CreateModel(
            name='Antecedant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anterieur_traitement', models.CharField(max_length=255)),
                ('ddr', models.DateField(null=True)),
                ('hta', models.CharField(max_length=255, null=True)),
                ('current_pregment', models.CharField(max_length=255, null=True)),
                ('diabete', models.CharField(max_length=255, null=True)),
                ('tabac', models.CharField(max_length=255, null=True)),
                ('alchool', models.CharField(max_length=255, null=True)),
                ('other', models.CharField(max_length=255, null=True)),
                ('visit_type', models.CharField(max_length=255, null=True)),
                ('churigical', models.CharField(max_length=255, null=True)),
                ('visite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='receptionspace.visite')),
            ],
        ),
    ]
