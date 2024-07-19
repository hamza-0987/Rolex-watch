from tinymce.models import HTMLField # type: ignore
from django.db import models
from django.db.models.manager import Manager


class Testimonial(models.Model):
    objects = Manager()
    name = models.CharField(max_length=100, verbose_name="Full Name")
    role = models.CharField(max_length=100, verbose_name="Role or Title")
    testimonial_text = HTMLField(verbose_name="Testimonial Text")  # Using HTMLField instead of TextField
    testimonial_date = models.DateField(verbose_name="Date of Testimonial")
    image = models.ImageField(upload_to='testimonials/', verbose_name="Profile Image")

 
