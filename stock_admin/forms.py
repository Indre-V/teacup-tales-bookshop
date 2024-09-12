"""Imports for Forms page"""
from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating a product.
    """
    class Meta:
        """
        Meta options for the ProductForm.
        Specifies the model to use and the fields to include in the form.
        """
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "border-primary border-2 h-12 p-2 w-full mb-2"}
            )

        self.fields["is_featured"].widget.attrs.update(
            {"class": "border-primary border-2"}
        )
