from django.db import models
from django import forms
from django.core.validators import EmailValidator
from django.utils import timezone
#mark_safe('<i class="fa fa-user" aria-hidden="true"></i>')
class ContactForm(models.Model):
    car_choices=(
         ('2.1','Comfort' ),('2.6','Van Comfort'),
         ('3.1','Black Limo'),
        )



    CHOICES = (('one','1'),('two','2'),('three','3'),('four','4'),('one','5'),('six','6'),)
        
    price = models.IntegerField(null=True,max_length=100)
    pick_up = models.CharField(null=True,max_length=100)
    drop_off = models.CharField(null=True,blank=False,max_length=100)
    pick_up_time=models.DateTimeField(default=timezone.now)  
    name = models.CharField(null=True,max_length=100)
    ride_type = models.CharField(max_length=20,choices=car_choices,default='1')
    
    passanger_count = models.CharField(max_length=10,choices=CHOICES,null=True,blank=True,default=1)
    email = models.CharField(null=True,blank=True,max_length=100,validators=[EmailValidator()])
    order_time=models.DateTimeField(default=timezone.now)
    phone = models.CharField(null=True,max_length=15)
    flight_nr = models.CharField(null=True,blank=True,max_length=100)
    Special_note = models.CharField(null=True,blank=True,max_length=100)


    def __str__(self):
        return self.name
    
    
 
    
    
    
    
    
    
    
    
    
