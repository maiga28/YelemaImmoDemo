from django import forms
from .models import CustomUser

class ProfileForm(forms.ModelForm):
    
    class Meta:
        
        model = CustomUser
        
        fields = ['bio', 'date_of_birth', 'phone_number', 'location', 'profile_picture']

