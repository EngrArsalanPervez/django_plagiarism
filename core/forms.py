from django import forms


class InputDocumentForm(forms.Form):
    query = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}))

