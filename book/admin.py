from django.contrib import admin
from .models import ContactForm
# Register your models here.


class FormAdmin(admin.ModelAdmin):
    list_filter = [
         "drop_off",
         "pick_up_time",
         "order_time"
    ]
    model=ContactForm
    list_display=('pick_up','drop_off','name', 'email', 'phone',"flight_nr",'Special_note')


admin.site.register(ContactForm, FormAdmin)
