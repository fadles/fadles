# coding=utf-8
from django import forms
from django.forms import ModelForm
from fadles.models import ContactUs

class ContactUsForm(ModelForm):
    # TODO: Redeclare lables
    name = forms.CharField(error_messages={'required': 'Пожалуйста введите свое имя'}, label='Ваше имя')
    email_or_phone = forms.CharField(error_messages={'required': 'Пожалуйста введите свой телефонный номер или email адрес'}
        , label='Телефон или электронная почта')
    message = forms.CharField(widget=forms.Textarea, error_messages={'required': 'Пожалуйста введите текст сообщения'}
        , label='Сообщение')

    exclude = ['datetime_created', 'moderated']

    class Meta:
        model = ContactUs