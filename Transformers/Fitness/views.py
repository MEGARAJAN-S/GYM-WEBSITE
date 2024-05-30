from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import register_table,user_table,trainer_table,trainer_attendance_table,fee_table
import datetime
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors,units
from reportlab.lib.styles import ParagraphStyle
# Create your views here.
Today = None
def today():
    global Today
    Today = datetime.date.today()
    fee_date_table = fee_table.objects.all()
    for data in fee_date_table:
        data.re_day = (data.end_date - Today).days - 1
        data.save()
def download_all_data_as_pdf(request):
    today()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="fee_table.pdf"'
    all_fee_data = fee_table.objects.all()
    table_data = [['GYM ID', 'NAME', 'PHONE', 'START DATE', 'END DATE', 'COUNTDOWN']]
    for data in all_fee_data:
        table_data.append([data.Gym_id, data.Name, data.phone, data.pay_date, data.end_date, data.re_day])
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE',(0,0),(-1,-1),15),
                        ('FONTSIZE',(0,1), (-1,-1),13),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BOTTOMPADDING', (0,1),(-1,-1),12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
                        ('GRID', (0, 0), (-1, -1), 2, colors.lightblue)])
    column_widths = [0.85*units.inch,1.55*units.inch,1.30*units.inch,1.4*units.inch,1.30*units.inch,1.4*units.inch]
    table = Table(table_data,colWidths=column_widths,rowHeights=26)
    table.setStyle(style)
    doc = SimpleDocTemplate(response)
    text = "FEE DETAILS"
    text_style = ParagraphStyle(name='Normal', fontSize=32, alignment=1, fontName='Helvetica-Bold')
    para = Paragraph(text, text_style)
    space = Spacer(1, 1*units.inch)
    space_one = Spacer(1, 0.5*units.inch)
    space_two = Spacer(1, 0.25*units.inch)
    global Today
    text_date = "DATE : " + str(Today)
    text_date_style = ParagraphStyle(name='Normal', fontSize=16, alignment=2)
    para_date = Paragraph(text_date, text_date_style)
    content = [para_date,space_one,para,space,table]
    doc.build(content)
    return response
def home(request):
    today()
    return render(request,'home.html')
def choice(request):
    return render(request,'choice.html')
def new(request):
    if request.method == "POST":
        name = request.POST['Name']
        phone = request.POST['Phone']
        email = request.POST['email']
        gym_id = "001"
        table_object = register_table.objects.values_list('Gym_id',flat=True)
        for data in table_object:
            if int(gym_id) <= int(data[1:]):
                gym_id = data[1:]
        ID = "T" + str(int(gym_id)+1)
        table = register_table(Gym_id=ID,Name=name,Phone=phone,email=email)
        table.save()
        return redirect('choice')
    today()
    return render(request,'new.html')
def register(request):
    if request.method == "POST":
        gym_id = request.POST['GymID']
        name = request.POST['Name']
        phone = request.POST['Phone']
        email = request.POST['email']
        table = register_table(Gym_id=gym_id,Name=name,Phone=phone,email=email)
        table.save()
        return redirect('choice')
    today()
    return render(request,'register.html')
def check_in_out(request):
    if request.method == "POST":
        check_in_out_id = request.POST["GymID"]
        check_out_data = user_table.objects.all()
        for data in check_out_data:
            if data.Gym_id == check_in_out_id and data.Out_time is None and data.attendance is True and data.Date == Today:
                check_out_id = data.Gym_id
                check_out_Name = data.Name
                check_out_in_time = data.In_time
                data.delete()
                check_out_table = user_table(
                    Gym_id=check_out_id,
                    Name=check_out_Name,
                    In_time=check_out_in_time,
                    Out_time=datetime.datetime.now().time(),
                    attendance=True
                )
                check_out_table.save()
                return redirect("check")
        check_in_data = register_table.objects.all()
        for data_in in check_in_data:
            if data_in.Gym_id == check_in_out_id:
                check_in_table = user_table(
                    Gym_id=check_in_out_id,
                    Name=data_in.Name,
                    In_time=datetime.datetime.now().time(),
                    attendance=True
                )
                check_in_table.save()
        return redirect("check")
    check_in_out_table = user_table.objects.filter(Date=Today)
    common_data = check_in_out_table.values_list('Gym_id',flat=True).distinct()
    fee_common_data = fee_table.objects.filter(Gym_id__in=common_data)
    today()
    return render(request,"check.html",{'user_data':check_in_out_table,'fee_data':fee_common_data})
def fee(request):
    if request.method == "POST":
        fee_gym_id = request.POST['GymID']
        fee_date = request.POST['Date']
        date_format = '%Y-%m-%d'
        real_date = datetime.datetime.strptime(fee_date,date_format).date()
        fee_value = fee_table.objects.all()
        for data in fee_value:
            if data.Gym_id == fee_gym_id:
                del_id = data.Gym_id
                del_name = data.Name
                del_phone = data.phone
                data.delete()
                value_table = fee_table(
                    Gym_id=del_id,
                    Name=del_name,
                    phone=del_phone,
                    pay_date=fee_date,
                    end_date=(real_date + datetime.timedelta(days=31)),
                    re_day=((real_date + datetime.timedelta(days=31)) - real_date).days,
                    paid=True
                )
                value_table.save()
                return redirect('fee')
        fee_data = register_table.objects.all()
        for data in fee_data:
            if data.Gym_id == fee_gym_id:
                fee_update_table = fee_table(
                    Gym_id=fee_gym_id,
                    Name=data.Name,
                    phone=data.Phone,
                    pay_date=fee_date,
                    end_date=(real_date+datetime.timedelta(days=30)),
                    re_day=((real_date+datetime.timedelta(days=30))-real_date).days,
                    paid=True
                )
                fee_update_table.save()
        return redirect('fee')
    fee_data_table = fee_table.objects.all()
    today()
    return render(request,'fee.html',{'feedata':fee_data_table})
def trainer(request):
    if request.method == "POST":
        Tid = request.POST["TID"]
        check_out_t_data = trainer_attendance_table.objects.all()
        for data in check_out_t_data:
            if data.T_id == Tid and data.out_time is None and data.date == Today:
                check_out_t_id = data.T_id
                check_out_t_name = data.Name
                check_out_t_in_time = data.in_time
                data.delete()
                check_out_t_table = trainer_attendance_table(
                    T_id=check_out_t_id,
                    Name=check_out_t_name,
                    in_time=check_out_t_in_time,
                    out_time=datetime.datetime.now().time(),
                    attendance=True
                )
                check_out_t_table.save()
                return redirect("trainer")
        check_in_t_data = trainer_table.objects.all()
        for data in check_in_t_data:
            if data.T_id == Tid:
                check_in_t_table = trainer_attendance_table(
                    T_id=data.T_id,
                    Name=data.Name,
                    in_time=datetime.datetime.now().time(),
                    attendance=True
                )
                check_in_t_table.save()
        return redirect("trainer")
    check_in_out_t_table = trainer_attendance_table.objects.filter(date=Today)
    today()
    return render(request,"trainer.html",{'Trainer':check_in_out_t_table})