import datetime

from django.db import models


class Sales(models.Model):
    slug = models.SlugField(max_length=20)
    start_date = models.DateField(
        default=datetime.date.today,
        help_text='First day of the survey'
    )
    end_date = models.DateField(
        default=datetime.date.today,
        help_text='Last day of the survey'
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.slug
