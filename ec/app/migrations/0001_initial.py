# Generated by Django 4.2.3 on 2023-07-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('vet', 'vetements'), ('chau', 'chaussures'), ('acc', 'accessoires'), ('b&c', 'Beauté & Cosmétique')], max_length=4)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]