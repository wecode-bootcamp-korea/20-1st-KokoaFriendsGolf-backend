from django.core.exceptions import ValidationError

class DuplicatedEntryError(Exception):
    def __init__(self, duplicated_field):
        super().__init__()
        self.err_message = f'Entry {duplicated_field} is duplicated.'

def validate_email(email):
    if not ("@" in email and "." in email):
        raise ValidationError(f"{email} is not an valid email.")

def validate_password(password):
    MIN_PASSWORD_LENGTH = 8

    if len(str(password)) < MIN_PASSWORD_LENGTH:
        raise ValidationError("Your Password is too short. Use Longer Password.")

def validate_gender(gender):
    if not gender:
        return 'N'

    if gender not in ['M', 'F']:
        raise ValidationError("Gender Field should be either 'M' or 'F' or empty.")

    return gender

def validate_duplicate(model, data):
    non_duplicatable_fields = [
        field.attname
        for field in model._meta.get_fields()
        if not field.is_relation and field.unique
    ]

    for field in non_duplicatable_fields:

        if field in data.keys():
            field_to_check = {field: data[field]}
            
            if model.objects.filter(**field_to_check).exists():
                raise DuplicatedEntryError(field)