from django import forms

class ProductSearchForm(forms.Form):
    title = forms.CharField(required=False, label='Title')
    author = forms.CharField(required=False, label='Author')
    description = forms.CharField(required=False, label='Description')
