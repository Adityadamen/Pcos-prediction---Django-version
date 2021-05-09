from django.urls import path
from . import views

app_name = 'predict'

urlpatterns = [
    path('',views.predict,name='predict'),
    path('predict/',views.practice,name='practice'),
    path('predict/result',views.result,name='result'),
]