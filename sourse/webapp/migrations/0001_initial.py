# Generated by Django 4.0.1 on 2022-01-08 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('text', models.TextField(blank=True, max_length=2000, verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.CharField(choices=[('active', 'Активная'), ('blocked', 'Заблокировано')], default='active', max_length=30, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
                'db_table': 'guest_book',
            },
        ),
    ]