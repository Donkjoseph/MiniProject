# Generated by Django 4.2.4 on 2023-09-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecohiveapp', '0043_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product_image',
            field=models.ImageField(default='C:\\Users\\donkj\\Downloads\\organic products\\tomato1.jpg', upload_to='product_images/'),
        ),
    ]