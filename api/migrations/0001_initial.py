# Generated by Django 5.1 on 2024-08-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('order_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'completed')], max_length=20)),
            ],
        ),
    ]
