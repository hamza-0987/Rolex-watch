# Generated by Django 5.0.7 on 2024-07-17 12:50

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Full Name")),
                (
                    "role",
                    models.CharField(max_length=100, verbose_name="Role or Title"),
                ),
                (
                    "testimonial_text",
                    tinymce.models.HTMLField(verbose_name="Testimonial Text"),
                ),
                (
                    "testimonial_date",
                    models.DateField(verbose_name="Date of Testimonial"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="testimonials/", verbose_name="Profile Image"
                    ),
                ),
            ],
        ),
    ]
