from django.db import models
from django.template.defaultfilters import truncatechars  # or truncatewords
from django.contrib.auth.admin import User
from phonenumber_field.modelfields import PhoneNumberField

class Exhibition(models.Model): # выставка
    title = models.CharField(verbose_name='Название', max_length=1000)
    description = models.TextField(verbose_name='Описание', blank=True, null = True)
    date_and_time = models.DateTimeField(verbose_name='Дата события', auto_now_add=False)

    def short_title(self):
        return f'{self.title[:50]} ...'

    def short_description(self):
        return f'{self.description[:100]} ...'

    def __str__(self):
        return f'{self.title}, {self.date_and_time}'

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставка'


class Author(models.Model): # автор
    full_name = models.CharField(verbose_name='Полное имя', max_length=1000)

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автор'


class Employee(models.Model): # сотрудник
    full_name = models.CharField(verbose_name='Полное имя', max_length=1000)
    post = models.CharField(verbose_name='Должность', max_length=215)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20)
    email = models.EmailField(verbose_name='Почта', blank=True)
    work_experience = models.TextField(verbose_name='Опыт работы')

    def __str__(self):
        return f'{self.full_name}, {self.post}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудник'


class Hall(models.Model): # зал
    hall_number = models.IntegerField(verbose_name='Номер зала')
    title = models.CharField(verbose_name='Название', max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'Зал № {self.hall_number} "{self.title}"'

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Зал'


class Museum_piece(models.Model): # экспонат
    piece_name = models.CharField(verbose_name='Название', max_length=1000)
    description = models.TextField(verbose_name='Описание', blank=True, null = True)
    date_of_creation = models.DateField(verbose_name='Дата создания', auto_now_add=False, blank=True, null = True)
    piece_type = models.TextField(verbose_name='Тип экспоната', blank=True, null = True)
    author_id = models.ForeignKey(Author, verbose_name='Автор', default=None, on_delete=models.CASCADE)
    hall_id = models.ForeignKey(Hall, verbose_name='Зал', default=None, on_delete=models.CASCADE)

    def short_title(self):
        return f'{self.piece_name[:50]} ...'

    def short_description(self):
        return f'{self.description[:100]} ...'

    def __str__(self):
        return f'{self.piece_name}, {self.piece_type}'

    class Meta:
        verbose_name = 'Экспонат'
        verbose_name_plural = 'Экспонат'


class Visitor(models.Model): # посетитель
    full_name = models.CharField(verbose_name='Полное имя', max_length=1000)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20)
    email = models.EmailField(verbose_name='Почта', blank=True)

    def __str__(self):
        return f'{self.full_name}, {self.email}'

    class Meta:
        verbose_name = 'Посетитель'
        verbose_name_plural = 'Посетитель'


class Exhibition_employee(models.Model): # Выставка Работник
    exhibition_id = models.ForeignKey(Exhibition, verbose_name='Выставка', default=None, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, verbose_name='Работник', default=None, on_delete=models.CASCADE)


class Exhibition_museum_piece(models.Model): # Выставка Экспонат
    exhibition_id =  models.ForeignKey(Exhibition, verbose_name='Выставка', default=None, on_delete=models.CASCADE)
    museum_piece_id =  models.ForeignKey(Museum_piece, verbose_name='Экспонат', default=None, on_delete=models.CASCADE)


class Exhibition_visitor(models.Model): # Выставка Посетитель
    exhibition_id = models.ForeignKey(Exhibition, verbose_name='Выставка', default=None, on_delete=models.CASCADE)
    visitor_id = models.ForeignKey(Visitor, verbose_name='Посетитель', default=None, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Почта', blank=True)


class Images(models.Model):
    piece = models.ForeignKey(Museum_piece, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')