# Generated by Django 4.0 on 2023-01-01 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Article', '0022_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddress',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
