# Generated by Django 4.2.4 on 2023-09-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_api', '0015_alter_transaction_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='user_id',
            field=models.CharField(default=None, max_length=200),
        ),
    ]