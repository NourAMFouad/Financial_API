# Generated by Django 4.2.4 on 2023-09-13 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial_api', '0011_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='user_profile',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_id_transaction', to='financial_api.userprofile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_id',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user_id',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
