# Generated by Django 4.0 on 2022-12-12 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0004_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='cap.png', upload_to='images/'),
            preserve_default=False,
        ),
    ]
