# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesFirst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название раздела')),
                ('slug', models.CharField(max_length=50, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name_plural': 'Раздел',
            },
        ),
        migrations.CreateModel(
            name='CategoriesSecond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название категирии')),
                ('slug', models.CharField(max_length=50, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название товара')),
                ('description', models.TextField(verbose_name='Описание')),
                ('size', models.CharField(max_length=50, verbose_name='Размер')),
                ('compound', models.CharField(max_length=100, verbose_name='Состав')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('land', models.CharField(max_length=50, verbose_name='Страна производитель')),
                ('image', models.ImageField(upload_to='img', verbose_name='Изображение товара')),
            ],
            options={
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
