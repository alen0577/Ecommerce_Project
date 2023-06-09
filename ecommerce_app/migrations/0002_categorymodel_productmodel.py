# Generated by Django 4.1.7 on 2023-03-29 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
                ('cat_img', models.ImageField(blank=True, null=True, unique=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pdes', models.CharField(max_length=250)),
                ('pimg', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('pprice', models.IntegerField()),
                ('pqty', models.IntegerField()),
                ('pcat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.categorymodel')),
            ],
        ),
    ]
