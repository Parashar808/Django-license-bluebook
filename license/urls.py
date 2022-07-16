from unicodedata import name
from django.urls import path,include
from . import views
from django.contrib import admin


urlpatterns=[

    path('',views.nationalid, name='nationalid'),
    path('license',views.license123,name='license123'),
    path('bluebook',views.bluebook123,name='bluebook123'),
    path('nationalid',views.nationalid,name='nationalid'),
    path('Fine',views.Fine,name='fine'),
    path('create1',views.create1,name='create1'),
    path('create2',views.create2,name='create2'),
    path('show1',views.show1,name='show1'),
    path('show2',views.show2,name='show2'),
    path('update1/<str:pk>/',views.update1,name='update1'),
    path('update2/<str:pk>/',views.update2,name='update2'),
    path('removea/<int:pk>', views.removea, name='removea'),
    path('removeb/<int:pk>', views.removeb, name='removeb'),





    
    # path('nationalidres',views.nationalidres,name='nationalidres'),


]
