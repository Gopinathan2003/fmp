# Generated by Django 5.1.6 on 2025-02-13 08:16

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.FloatField(default=0)),
                ('date', models.DateField(default=datetime.date(2025, 2, 13))),
                ('long_term', models.BooleanField(default=False)),
                ('interest_rate', models.FloatField(blank=True, default=0, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('monthly_expenses', models.FloatField(blank=True, default=0, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('expense', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('expense_list', models.ManyToManyField(blank=True, to='ExpenseTracker.expense')),
            ],
        ),
    ]
