# Generated by Django 4.2.1 on 2023-06-20 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('NB', 'Lipa na Mpesa'), ('PP', 'Cash')], max_length=2),
        ),
    ]
