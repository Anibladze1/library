# Generated by Django 4.2.5 on 2023-09-30 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="book_images"),
        ),
    ]
