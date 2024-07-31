# Generated by Django 5.0.7 on 2024-07-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phone_num', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
