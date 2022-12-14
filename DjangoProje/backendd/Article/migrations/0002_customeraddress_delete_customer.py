# Generated by Django 4.0 on 2022-12-06 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_title', models.CharField(max_length=50)),
                ('address_line', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('customer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
