from dataclasses import field
from django import forms
from.models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'
    
    
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        widgets={
            'booking_date':DateInput
            
        }