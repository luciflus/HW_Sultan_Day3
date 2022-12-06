# Generated by Django 3.2 on 2022-12-06 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='ФИО клиента')),
                ('citizenship', models.CharField(default='Кыргызстан', max_length=20, verbose_name='гражданство')),
                ('birth_year', models.DateField(verbose_name='год рождения')),
                ('work_place', models.CharField(max_length=30, null=True, verbose_name='место работы')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='дата последнего обновления')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField(verbose_name='сумма кредита')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='дата получения кредита')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='credit.client')),
            ],
            options={
                'verbose_name': 'Кредит',
                'verbose_name_plural': 'Кредиты',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, verbose_name='номер аккаунта')),
                ('account_type', models.IntegerField(default=1, verbose_name='тип аккаунта')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='credit.client')),
            ],
            options={
                'verbose_name': 'Счет',
                'verbose_name_plural': 'Счета',
                'db_table': 'accounts',
            },
        ),
    ]
