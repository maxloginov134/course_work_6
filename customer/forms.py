from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError
from validate_email import validate_email

from customer.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'comment')

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

    def clean_email(self):
        new_email = self.cleaned_data['email']
        if Customer.objects.filter(email=new_email).exists():
            raise ValidationError('Почта уже занята')
        if validate_email(new_email, verify=True) is None:
            raise ValidationError('Почты не существует')
        return new_email


class UpdateCustomerForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'comment')

    def __init__(self, *args, **kwargs):
        super(UpdateCustomerForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'