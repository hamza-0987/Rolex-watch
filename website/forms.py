from django import forms
from contactus.models import Contact

class SumForm(forms.Form):
    number1 = forms.IntegerField(label='Number 1', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    number2 = forms.IntegerField(label='Number 2', widget=forms.NumberInput(attrs={'class': 'form-control'}))



class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class CalculatorForm(forms.Form):
    number1 = forms.FloatField(label='Number 1', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    number2 = forms.FloatField(label='Number 2', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    operation = forms.ChoiceField(label='Operation', choices=[('+', 'Add'), ('-', 'Subtract'), ('*', 'Multiply'), ('/', 'Divide')], widget=forms.Select(attrs={'class': 'form-control'}))


   

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

