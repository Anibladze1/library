# Generated by Django 4.2.5 on 2023-09-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="condition", name="is_new",),
        migrations.AddField(
            model_name="condition",
            name="condition",
            field=models.CharField(
                choices=[("New", "New"), ("Used", "Used")], default="New", max_length=10
            ),
        ),
    ]