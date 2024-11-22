from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('parse',views.parse,name='parse'),
    path('xlMaker',views.xlMaker,name='xlMaker')
]
