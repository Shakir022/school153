# Generated by Django 4.2.7 on 2023-12-08 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_birthday_alter_customuser_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='name',
            field=models.CharField(max_length=20, verbose_name='класс'),
        ),
    ]