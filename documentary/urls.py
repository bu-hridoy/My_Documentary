
from django.urls import path,include
from . import views

urlpatterns = [
    #path('', views.index , name='index'),
    path('',views.data_form,name='insert'),
    path('<int:id>/',views.data_form,name='update'),
    path('delete/<int:id>/',views.data_delete,name='delete'),
    path('show/',views.data_list,name='list')
]