from django import forms
from website.models import Contact
from simplemathcaptcha.fields import MathCaptchaField


class ContactForm(forms.ModelForm):
    captcha = MathCaptchaField()
    class Meta:
        model = Contact
        fields ='__all__'