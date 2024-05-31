from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    r'^\+?1?\d{9,15}$',
    'Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.'
)
