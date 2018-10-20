from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
#PRODUCT_SIZE_CHOICES = ['XS','S','M','L','XL','XXL','XXXL']
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    #size = forms.CharField(label="SIZE",widget=forms.Select(PRODUCT_QUANTITY_CHOICES))
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
