from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_attrs(value):
    if value < 1 or value > 20:
        raise ValidationError(_('%(value) has to be greater than 1 and lesser than 21'),
                              params={'value': value},
                              )