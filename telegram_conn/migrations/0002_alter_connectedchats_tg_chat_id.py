# Generated by Django 4.2.4 on 2023-08-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_conn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectedchats',
            name='tg_chat_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='id чата телеграм'),
        ),
    ]
