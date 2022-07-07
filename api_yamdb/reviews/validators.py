from datetime import datetime as dt

from django.core.exceptions import ValidationError


def validate_year(year):
    if year > dt.now().year:
        raise ValidationError(
            'Year should\'t be in future'
        )
