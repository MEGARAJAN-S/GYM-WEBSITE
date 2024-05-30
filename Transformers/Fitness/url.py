from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home/choice',views.choice,name='choice'),
    path('home/choice/register',views.register,name='register'),
    path('home/choice/new',views.new,name='new'),
    path('home/check',views.check_in_out,name='check'),
    path('home/fee',views.fee,name='fee'),
    path('home/check/trainer',views.trainer,name='trainer'),
    path('download',views.download_all_data_as_pdf,name='download'),
]