from django.urls import path
from . import views
app_name = 'faculty'

urlpatterns = [
    path('', views.faculties_view, name='faculties'),
    path('chair', views.chairs_view, name='chairs')

]