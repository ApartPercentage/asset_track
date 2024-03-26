from django import forms
from .models import Assets, BorrowTransaction

class AssetsForm(forms.ModelForm):
    class Meta:
        model = Assets
        fields = ['name', 'category', 'serial_number', 'description', 'note']

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Assets
        #fields = ['asset']
        fields = ['asset']

    asset = forms.ModelMultipleChoiceField(queryset=Assets.objects.all().order_by('name'), widget=forms.SelectMultiple(attrs={'placeholder': 'Select'}), label = 'Search and borrow...')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['asset'].queryset = Assets.objects.filter(is_available=True).order_by('name')
        ##self.fields['asset'].queryset = Assets.objects.all().order_by('name')

    def clean_asset(self):
    #    '''item = self.cleaned_data.get('asset')
    #    if not item.is_available:
    #        borrow_record = BorrowTransaction.objects.filter(asset=item, date_returned=None).first()

    #        if borrow_record:  # Check if a borrow record exists
    #            raise forms.ValidationError(f"This asset is currently not available (borrowed by {borrow_record.staff_member})")
    #        else:  
    #            raise forms.ValidationError("This asset is currently not available.")  # Generic message if no active borrow record found
    #        #raise forms.ValidationError("This asset is currently not available")
    #    return item'''
        chosen_assets = self.cleaned_data.get('asset')
        unavailable_assets = []

        for item in chosen_assets:
            if not item.is_available:
                borrow_record = BorrowTransaction.objects.filter(asset=item, date_returned=None).first()
                if borrow_record:  # Check if a borrow record exists
                    unavailable_assets.append(f"{item} (borrowed by {borrow_record.staff_member})")
            else:
                borrow_record = None

        if unavailable_assets:
            if len(unavailable_assets) == 1:
                message = f"This asset is currently not available: {unavailable_assets[0]}"
            else:
                message = f"The following assets are currently not available:\n - {', '.join(unavailable_assets)}"
            raise forms.ValidationError(message)

        return chosen_assets