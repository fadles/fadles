# coding=utf-8
from django import forms
from django.forms import ModelForm
from fadles.models import ContactUs

class ContactUsForm(ModelForm):
    # TODO: Redeclare lables
    name = forms.CharField(error_messages={'required': 'Пожалуйста введите свое имя'})
    email = forms.EmailField(error_messages={'required': 'Пожалуйста введите свой email',
                                             'invalid': 'Пожалуйста введите правильный email адрес'})
    phone = forms.CharField(error_messages={'required': 'Пожалуйста введите свой телефонный номер'})
    message = forms.CharField(widget=forms.Textarea, error_messages={'required': 'Пожалуйста введите текст сообщения'})

    exclude = ['datetime_created', 'moderated']

    class Meta:
        model = ContactUs