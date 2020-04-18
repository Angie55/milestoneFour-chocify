from django import forms


class ContactForm(forms.Form):
    """ Form for customers to fill and contact
     using emailjs
     """

    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 12,
            },
        ),
    )

    class Meta:
        fields = [
            'name',
            'email',
            'message',
        ]
