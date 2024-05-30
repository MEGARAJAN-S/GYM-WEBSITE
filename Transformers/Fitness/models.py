from django.db import models

# Create your models here.
class user_table(models.Model):
    Gym_id = models.CharField(max_length=5)
    Name = models.CharField(max_length=100)
    Date = models.DateField(auto_now=True)
    In_time = models.TimeField(blank=True, null=True)
    Out_time = models.TimeField(blank=True, null=True)
    attendance = models.BooleanField(default=False)
class register_table(models.Model):
    Gym_id = models.CharField(max_length=5)
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    email = models.EmailField()
class fee_table(models.Model):
    Gym_id = models.CharField(max_length=5)
    Name = models.CharField(max_length=100)
    phone = models.IntegerField()
    pay_date = models.DateField()
    end_date = models.DateField()
    re_day = models.IntegerField()
    paid = models.BooleanField()
class trainer_table(models.Model):
    T_id = models.CharField(max_length=10)
    Name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
class trainer_attendance_table(models.Model):
    T_id = models.CharField(max_length=10)
    Name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    in_time = models.TimeField(blank=True,null=True)
    out_time = models.TimeField(blank=True,null=True)
    attendance = models.BooleanField()

