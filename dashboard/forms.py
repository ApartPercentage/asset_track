from django import forms
from .models import Assets, BorrowTransaction

class AssetsForm(forms.ModelForm):
    class Meta:
        model = Assets
        fields = ['name', 'category', 'serial_number', 'description', 'note']

class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowTransaction
        fields = ['asset']

    def clean_asset(self):
        item = self.cleaned_data.get('asset')
        if not item.is_available:
            borrow_record = BorrowTransaction.objects.filter(asset=item, date_returned=None).first()

            if borrow_record:  # Check if a borrow record exists
                raise forms.ValidationError(f"This asset is currently not available (borrowed by {borrow_record.staff_member})")
            else:  
                raise forms.ValidationError("This asset is currently not available.")  # Generic message if no active borrow record found
            #raise forms.ValidationError("This asset is currently not available")
        return item