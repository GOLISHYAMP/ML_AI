from django import forms

class add_items(forms.Form):
    item_name = forms.CharField(max_length=10,required=True)
    quantity = forms.IntegerField(min_value=0)