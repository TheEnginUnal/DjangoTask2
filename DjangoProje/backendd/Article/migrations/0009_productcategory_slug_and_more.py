# Generated by Django 4.0 on 2022-12-15 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0008_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(default='product', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='categoryName',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
