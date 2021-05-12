from django.db           import models
from django.forms.models import model_to_dict

class User(models.Model):

    created_at   = models.DateTimeField(auto_now_add=True)
    email        = models.EmailField("user email", max_length=254, unique=True, blank=False)
    password     = models.CharField("user password", max_length=65, blank=False)
    phone_number = models.CharField("user phone number", max_length=17, unique=True, blank=False)
    name         = models.CharField("user's name", max_length=20, blank=False)
    birthday     = models.DateField("user's birthday", blank=True, null=True)
    gender       = models.CharField("user's gender", max_length=1)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.id}: {self.email} | {self.name}'

    def to_dict(self):
        model_dict = model_to_dict(self)
        model_dict.pop("password")
        return model_dict
