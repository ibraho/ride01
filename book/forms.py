from django import forms
from.models import *
from django.contrib import admin
from django.utils.safestring import mark_safe

class ConForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        widgets = {
                'pick_up_time': forms.widgets.DateInput(attrs={'type': 'datetime-local'}),
                'pick_up': forms.widgets.TextInput(attrs={'placeholder': 'Your Adress'}),
                'drop_off': forms.widgets.TextInput(attrs={'placeholder': 'Destination'}),
                
                'name': forms.widgets.TextInput(attrs={'placeholder': 'Your Name'}),
                'email': forms.widgets.TextInput(attrs={'placeholder': 'Email Address'}),
                'phone': forms.widgets.TextInput(attrs={'placeholder': 'Your Phone Nr'}),
                'flight_nr': forms.widgets.TextInput(attrs={'placeholder': 'Flight Nr (Coming From Airport)'}),
                'Special_note': forms.widgets.TextInput(attrs={'placeholder': ' Instructions For The Driver Or Requests'}),
               # 'pick_up_time': forms.widgets.TextInput(attrs={'placeholder': 'Time For Pick Up'}),
                
                
        }

        fields = "__all__"
        exclude = ('order_time',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pick_up'].widget.attrs.update({'id':'from'}),
        self.fields['drop_off'].widget.attrs.update({'id':'to'}),
        self.fields['name'].widget.attrs.update({'id':'name'}),
        self.fields['email'].widget.attrs.update({'id':'email'}),
        self.fields['phone'].widget.attrs.update({'id':'phone'}),
        self.fields['flight_nr'].widget.attrs.update({'id':'flight'}),
        self.fields['Special_note'].widget.attrs.update({'id':'note'}),
        self.fields['pick_up_time'].widget.attrs.update({'id':'datepickeru',}),
        


       
