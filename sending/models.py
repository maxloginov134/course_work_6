from datetime import datetime

from django.db import models

from customer.models import Customer
from users.models import User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    theme = models.CharField(max_length=50, verbose_name='Тема')
    content = models.TextField(verbose_name='Контент')

    def __str__(self):
        return f'{self.theme}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Sending(models.Model):
    ONE_A_DAY = 'раз в день'
    ONE_A_WEEK = 'раз в неделю'
    ONE_A_MONTH = 'раз в месяц'

    INTERVAL = (
        (ONE_A_DAY, 'раз в день'),
        (ONE_A_WEEK, 'раз в неделю'),
        (ONE_A_MONTH, 'раз в месяц')
    )
    COMPLITED = 'Завершена'
    CREATED = 'Создана'
    ACTIVATED = 'Запущена'

    STATUS = (
        (COMPLITED, 'завершена'),
        (CREATED, 'создана'),
        (ACTIVATED, 'активирована')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    customer = models.ManyToManyField(Customer, verbose_name='Клиент')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name='Сообщение', null=True)
    created_at = models.DateTimeField(editable=True, auto_now=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(editable=True, auto_now=True, verbose_name='Время обновления')
    next_run = models.DateTimeField(editable=True, auto_now=True, verbose_name='Дата следующей рассылки')
    interval = models.CharField(choices=INTERVAL, max_length=30, verbose_name='Периодичность')
    status_sending = models.CharField(choices=STATUS, max_length=30, verbose_name='Статус')
    start_sending_date = models.DateField(default=datetime.today(), verbose_name='Дата начала')
    start_sending_time = models.TimeField(default=datetime.now().time(), verbose_name='время рассылки', blank=True,
                                          null=True)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

        permissions = [
            (
                'can_view_sending',
                'Can view sending'
            ),
            (
                'can_disable_sending',
                'Can disable sending'
            )
        ]

    def get_customer(self):
        return ','.join([str(cus) for cus in self.customer.all()])


class TrySending(models.Model):
    STATUS_CHOICES = [
        ('success', 'завершена'),
        ('failure', 'провалена'),
        ('in_progress', 'в процессе'),
    ]

    sending = models.ForeignKey(Sending, on_delete=models.CASCADE, verbose_name='Письмо', blank=True, null=True)
    last_attempt = models.DateTimeField(auto_now_add=True, verbose_name='Дата последней попытки')
    status_attempt = models.CharField(choices=STATUS_CHOICES, max_length=30, default='in_progress',
                                      verbose_name='Текущий статус')
    answer_server = models.CharField(max_length=20, verbose_name='Ответ почтового сервера')

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылок'
