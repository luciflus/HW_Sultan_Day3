from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=20, null=False, verbose_name='ФИО клиента')
    citizenship = models.CharField(max_length=20, null=False, default='Кыргызстан', verbose_name='гражданство')
    birth_year = models.DateField(null=False, verbose_name='год рождения')
    work_place = models.CharField(max_length=30, null=True, verbose_name='место работы')
    update_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего обновления')

    class Meta:
        db_table = 'customers'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name

class Account(models.Model):
    number = models.CharField(max_length=16, null=False, verbose_name='номер аккаунта')
    account_type = models.IntegerField(default=1, null=False, verbose_name='тип аккаунта')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="accounts")

    class Meta:
        db_table = 'accounts'
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return self.number

class Credit(models.Model):
    sum = models.IntegerField(null=False, verbose_name='сумма кредита')
    date = models.DateTimeField(auto_now=True, verbose_name='дата получения кредита')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="credits")

    class Meta:
        db_table = 'loans'
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'

    def __str__(self):
        return self.sum