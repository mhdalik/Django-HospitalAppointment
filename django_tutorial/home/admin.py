from django.contrib import admin
from.models import Departments, Doctors, Booking
from import_export.admin import ImportExportModelAdmin
# Register your models here.

#admin.site.register(Departments)

@admin.register(Departments)
class userdat(ImportExportModelAdmin):
    pass

admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('doc_name','id','p_name','p_phone','p_email','booking_date','booked_on')
    
admin.site.register(Booking, BookingAdmin)


