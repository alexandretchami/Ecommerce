# Generated by Django 4.2.3 on 2023-07-29 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('vet', 'vetements'), ('chau', 'chaussures'), ('acc', 'accessoires'), ('bc', 'Beauté & Cosmétique')], max_length=4),
        ),
    ]