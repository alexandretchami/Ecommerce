# Generated by Django 4.2.3 on 2023-07-29 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('jea', 'jeans'), ('chau', 'chaussures'), ('jup', 'jupes'), ('pul', 'pulls'), ('top', 'T-shirts'), ('vest', 'vestes'), ('blaz', 'blazers'), ('acc', 'accessoires'), ('bc', 'Beauté & Cosmétique')], max_length=9),
        ),
    ]
