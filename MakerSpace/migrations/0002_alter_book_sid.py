# Generated by Django 4.1.4 on 2023-03-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MakerSpace", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="sid",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]