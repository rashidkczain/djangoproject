from django.urls import path
from.import views
app_name='app2'
urlpatterns=[
    path('',views.index,name='index'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('gallery',views.gallery,name='gallery'),
    path('detailes/<int:id>',views.detailes,name='detailes')
]