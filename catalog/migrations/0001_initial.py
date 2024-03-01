# Generated by Django 5.0.2 on 2024-03-01 21:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Продукт (Вещь?)')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='Фото')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Цена')),
                ('created_date', models.DateField(verbose_name='Дата создания')),
                ('date_of_last_changes', models.DateTimeField(verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
            options={
                'verbose_name': 'Продукт (Вешь?)',
                'verbose_name_plural': 'Продукты (Вещи?)',
            },
        ),
    ]