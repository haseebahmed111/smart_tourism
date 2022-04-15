from django import forms

from apps.home.models import City
from tour_guide.models import TourGuideProfile, Language


class TourGuideProfileFrom(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Full Name",
                "class": "form-control"
            }
        ))
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "City",
                "class": "form-control"
            }
        ))
    languages = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Languages you know",
                "class": "form-control"
            }
        ))
    brief_info = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "About",
                "class": "form-control"
            }
        ))
    mobile_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Contact Number",
                "class": "form-control"
            }
        ))
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address of Office",
                "class": "form-control"
            }
        ))
    policy = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Policy",
                "class": "form-control"
            }
        ))
    terms_and_condition = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Terms and Conditions",
                "class": "form-control"
            }
        ))

    picture = forms.ImageField(required=False)

    class Meta:
        model = TourGuideProfile
        fields = (
            'name', 'city', 'languages', 'brief_info', 'mobile_number', 'address', 'policy', 'terms_and_condition',
            'picture')


class LanguageFrom(forms.ModelForm):
    language_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name of Language",
                "class": "form-control"
            }
        ))
    native = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = Language
        fields = ('language_name', 'native')
