from django import forms

class IndexForm(forms.Form):
    search = forms.CharField(label='Search people', widget=forms.TextInput(attrs={'placeholder': 'Ex: Nara Lemos'}))
