# Generated by Django 4.2.4 on 2023-09-12 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_api', '0006_delete_registered_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='user_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
