from django import forms
from .models import CustomerReview


class CustomerReviewForm(forms.ModelForm):
    class Meta:
        model = CustomerReview
        fields = ['name', 'rating', 'is_customer', 'comment']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'rating': 'Rating 0-5',
            'is_customer': 'Customer',
            'comment': 'Comment/Review',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rating':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
        self.fields[field].label = False
