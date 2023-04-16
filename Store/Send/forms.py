from django.forms import ModelForm
from django.forms import Textarea
from .models import SendForm


class ContactForm(ModelForm):

    class Meta:
        model = SendForm
        fields = '__all__'
