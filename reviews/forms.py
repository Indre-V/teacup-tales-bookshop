"""Review Form imports"""
from django import forms
from .models import Review


class ReviewProductForm(forms.ModelForm):
    """
    A form for creating and updating roduct reviews.
    """
    content = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={
            'rows': 5,
            'cols': 30
        })
    )

    class Meta:
        """
        Meta options for the CommentForm.
        Specifies the model to use and the fields to include in the form.
        """
        model = Review
        fields = ['rating', 'content']
