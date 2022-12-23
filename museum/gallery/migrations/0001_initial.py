# Generated by Django 2.2 on 2022-11-19 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=1000, verbose_name='Полное имя')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Автор',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=1000, verbose_name='Полное имя')),
                ('post', models.CharField(max_length=215, verbose_name='Должность')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Почта')),
                ('work_experience', models.TextField(verbose_name='Опыт работы')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудник',
            },
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('date_and_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата события')),
            ],
            options={
                'verbose_name': 'Выставка',
                'verbose_name_plural': 'Выставка',
            },
        ),
        migrations.CreateModel(
            name='Exhibition_employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exhibition_id', models.IntegerField(verbose_name='Выставка')),
                ('employee_id', models.IntegerField(verbose_name='Работник')),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition_museum_piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exhibition_id', models.IntegerField(verbose_name='Выставка')),
                ('museum_piece_id', models.IntegerField(verbose_name='Экспонат')),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition_visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exhibition_id', models.IntegerField(verbose_name='Выставка')),
                ('visitor_id', models.IntegerField(verbose_name='Посетитель')),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_number', models.IntegerField(verbose_name='Номер зала')),
                ('title', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Зал',
            },
        ),
        migrations.CreateModel(
            name='Museum_piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece_name', models.CharField(max_length=1000, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('piece_type', models.TextField(blank=True, null=True, verbose_name='Тип экспоната')),
                ('author_id', models.IntegerField(blank=True, null=True, verbose_name='Автор')),
                ('hall_id', models.IntegerField(verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Экспонат',
                'verbose_name_plural': 'Экспонат',
            },
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=1000, verbose_name='Полное имя')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Посетитель',
                'verbose_name_plural': 'Посетитель',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Почта')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gallery.Museum_piece')),
            ],
        ),
    ]
