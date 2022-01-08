from django.db import models

# Create your models here.
STATUS_CHOICES = [('active', 'Активная'), ('blocked', 'Заблокировано')]

class Book(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Имя')
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name='Email')
    text = models.TextField(max_length=2000, null=False, blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    status = models.CharField(max_length=30, null=False, blank=False, default="active", choices=STATUS_CHOICES, verbose_name='Статус')

    def __str__(self):
        return f'{self.pk}) {self.name} : {self.email} / {self.updated_at} | {self.status}'

    class Meta:
        db_table = 'guest_book'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
