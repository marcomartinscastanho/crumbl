# Generated by Django 4.2 on 2024-03-05 16:49

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("name", models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]
