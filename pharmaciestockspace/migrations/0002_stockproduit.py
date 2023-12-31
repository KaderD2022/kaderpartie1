# Generated by Django 4.1.7 on 2023-10-13 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminspace', '0003_user_state'),
        ('pharmaciestockspace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminspace.collaborateur')),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmaciestockspace.produit')),
            ],
        ),
    ]
