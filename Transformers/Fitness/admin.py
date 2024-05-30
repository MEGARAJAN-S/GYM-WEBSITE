from django.contrib import admin
from .models import register_table
from .models import fee_table
from .models import user_table
from .models import trainer_table
from .models import trainer_attendance_table
# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('Gym_id', 'Name', 'Phone', 'email')
    list_filter = ('Gym_id', 'Name', 'Phone')
admin.site.register(register_table,RegisterAdmin)
class UserAdmin(admin.ModelAdmin):
    list_display = ('Gym_id', 'Name', 'Date', 'In_time', 'Out_time', 'attendance')
    list_filter = ('Date', 'In_time', 'Out_time', 'attendance')
admin.site.register(user_table,UserAdmin)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('Gym_id', 'Name', 'phone', 'pay_date', 'end_date', 're_day')
    list_filter = ('Gym_id', 'pay_date', 'end_date', 're_day')
admin.site.register(fee_table,FeeAdmin)
class TrainerRegisterAdmin(admin.ModelAdmin):
    list_display = ('T_id', 'Name', 'phone', 'email')
    list_filter = ('T_id', 'Name')
admin.site.register(trainer_table,TrainerRegisterAdmin)
class TrainerAttendanceAdmin(admin.ModelAdmin):
    list_display = ('T_id', 'Name', 'date', 'in_time', 'out_time', 'attendance')
    list_filter = ('date', 'in_time', 'out_time', 'attendance')
admin.site.register(trainer_attendance_table,TrainerAttendanceAdmin)
