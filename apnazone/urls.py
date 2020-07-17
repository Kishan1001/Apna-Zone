from django.urls import path, include
from apnazone.views import Welcome
from apnazone import views


app_name = 'apnazone'

urlpatterns = [
    path('', views.Welcome, name='home'),


]