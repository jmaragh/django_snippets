from django.core.validators import RegexValidator
from django.forms import CharField
from django.forms.widgets import TextInput

class PhoneField(CharField):
    widget = TextInput
    default_validators = [RegexValidator(r"^\d{3,4}-\d{3}-\d{4}$", "Invalid Phone number")]

    def __init__(self, **kwargs):
        return super().__init__(strip=True, **kwargs)
