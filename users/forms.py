from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _

from users.models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    last_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Last Name',
                                widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'})))
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})))
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),
                                help_text=_('Just Enter the same password, for confirmation'))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'avatar')
        exclude = ('password',)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['password'].widget.attrs['hidden'] = True

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserBlockedForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)
